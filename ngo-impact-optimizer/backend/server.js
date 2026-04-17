const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

const DATASET_PATH = path.join(__dirname, '..', 'dataset', 'ngo_impact_cleaned.csv');

const fallbackPrograms = [
    {
        id: 1,
        ngoName: 'Community Learning Trust',
        programType: 'Education',
        location: 'India',
        cost: 5200,
        peopleHelped: 260,
        outcomeScore: 8.7
    },
    {
        id: 2,
        ngoName: 'HealthBridge Initiative',
        programType: 'Healthcare',
        location: 'Kenya',
        cost: 8400,
        peopleHelped: 190,
        outcomeScore: 9.1
    },
    {
        id: 3,
        ngoName: 'Harvest Hope Network',
        programType: 'Food Security',
        location: 'Brazil',
        cost: 4100,
        peopleHelped: 340,
        outcomeScore: 7.9
    },
    {
        id: 4,
        ngoName: 'Green Future Alliance',
        programType: 'Environment',
        location: 'Nigeria',
        cost: 6800,
        peopleHelped: 210,
        outcomeScore: 8.4
    }
];

function parseCsvLine(line) {
    const fields = [];
    let current = '';
    let inQuotes = false;

    for (let index = 0; index < line.length; index += 1) {
        const char = line[index];
        const next = line[index + 1];

        if (char === '"' && inQuotes && next === '"') {
            current += '"';
            index += 1;
        } else if (char === '"') {
            inQuotes = !inQuotes;
        } else if (char === ',' && !inQuotes) {
            fields.push(current.trim());
            current = '';
        } else {
            current += char;
        }
    }

    fields.push(current.trim());
    return fields;
}

function toNumber(value, defaultValue = 0) {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : defaultValue;
}

function loadProgramsFromCsv(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8').trim();
        if (!content) {
            return [];
        }

        const lines = content.split(/\r?\n/).filter(Boolean);
        const headers = parseCsvLine(lines[0]).map((header) => header.toLowerCase());

        const programs = lines.slice(1).map((line, rowIndex) => {
            const fields = parseCsvLine(line);
            const row = {};

            headers.forEach((header, fieldIndex) => {
                row[header] = fields[fieldIndex] || '';
            });

            return {
                id: rowIndex + 1,
                ngoName: row.ngo_name || row.ngoname || `NGO_${rowIndex + 1}`,
                programType: row.program_type || row.programtype || 'Uncategorized',
                location: row.location || 'Unknown',
                cost: toNumber(row.cost),
                peopleHelped: toNumber(row.people_helped),
                outcomeScore: toNumber(row.outcome_score)
            };
        });

        return programs.filter((program) => program.cost > 0 && program.peopleHelped >= 0);
    } catch (error) {
        console.error('Failed to load CSV dataset. Falling back to sample data.', error.message);
        return [];
    }
}

let ngoPrograms = loadProgramsFromCsv(DATASET_PATH);
if (!ngoPrograms.length) {
    ngoPrograms = fallbackPrograms;
}

app.use(cors());
app.use(express.json());

function withImpactScore(program) {
    const impactScore = (program.peopleHelped * program.outcomeScore) / program.cost;
    return {
        ...program,
        impactScore: Number(impactScore.toFixed(5))
    };
}

function applyFilters(programs, query) {
    const programType = (query.programType || '').trim();
    const location = (query.location || '').trim();
    const search = (query.search || '').trim().toLowerCase();
    const minOutcomeScore = toNumber(query.minOutcomeScore, 0);
    const maxCost = query.maxCost ? toNumber(query.maxCost, Number.MAX_SAFE_INTEGER) : Number.MAX_SAFE_INTEGER;
    const minPeopleHelped = toNumber(query.minPeopleHelped, 0);

    return programs.filter((program) => {
        const matchesProgramType = !programType || programType === 'All' || program.programType === programType;
        const matchesLocation = !location || location === 'All' || program.location === location;
        const matchesOutcome = program.outcomeScore >= minOutcomeScore;
        const matchesCost = program.cost <= maxCost;
        const matchesPeople = program.peopleHelped >= minPeopleHelped;
        const matchesSearch =
            !search ||
            program.ngoName.toLowerCase().includes(search) ||
            program.programType.toLowerCase().includes(search) ||
            program.location.toLowerCase().includes(search);

        return matchesProgramType && matchesLocation && matchesOutcome && matchesCost && matchesPeople && matchesSearch;
    });
}

function buildOverviewFromPrograms(programs) {
    const rankedPrograms = programs
        .map(withImpactScore)
        .sort((a, b) => b.impactScore - a.impactScore);

    const totalBudget = programs.reduce((sum, program) => sum + program.cost, 0);
    const totalPeopleHelped = programs.reduce((sum, program) => sum + program.peopleHelped, 0);
    const avgOutcomeScore =
        programs.length > 0
            ? programs.reduce((sum, program) => sum + program.outcomeScore, 0) / programs.length
            : 0;

    return {
        metrics: {
            programsAnalyzed: programs.length,
            totalBudget,
            totalPeopleHelped,
            avgOutcomeScore: Number(avgOutcomeScore.toFixed(2))
        },
        topProgram: rankedPrograms[0] || null,
        categories: [...new Set(programs.map((program) => program.programType))],
        locations: [...new Set(programs.map((program) => program.location))]
    };
}

app.get('/', (req, res) => {
    res.json({ message: "NGO Impact Optimizer API is running..." });
});

app.get('/api/health', (req, res) => {
    res.json({
        status: 'ok',
        service: 'ngo-impact-optimizer-backend',
        timestamp: new Date().toISOString()
    });
});

app.get('/api/programs', (req, res) => {
    const filteredPrograms = applyFilters(ngoPrograms, req.query);
    const rankedPrograms = filteredPrograms
        .map(withImpactScore)
        .sort((a, b) => b.impactScore - a.impactScore);

    const limit = req.query.limit ? toNumber(req.query.limit, rankedPrograms.length) : rankedPrograms.length;
    const programs = rankedPrograms.slice(0, limit);

    res.json({
        count: programs.length,
        totalMatches: rankedPrograms.length,
        programs
    });
});

app.get('/api/overview', (req, res) => {
    const filteredPrograms = applyFilters(ngoPrograms, req.query);
    res.json(buildOverviewFromPrograms(filteredPrograms));
});

app.get('/api/filters', (req, res) => {
    const categories = [...new Set(ngoPrograms.map((program) => program.programType))].sort();
    const locations = [...new Set(ngoPrograms.map((program) => program.location))].sort();
    const maxCost = ngoPrograms.reduce((max, program) => Math.max(max, program.cost), 0);

    res.json({
        categories,
        locations,
        ranges: {
            minOutcomeScore: 0,
            maxOutcomeScore: 10,
            maxCost
        }
    });
});

app.post('/api/reload', (req, res) => {
    const refreshed = loadProgramsFromCsv(DATASET_PATH);
    if (refreshed.length) {
        ngoPrograms = refreshed;
        res.json({ status: 'ok', recordsLoaded: ngoPrograms.length });
        return;
    }

    res.status(500).json({ status: 'error', message: 'Failed to reload dataset from CSV.' });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
