import React, { useEffect, useMemo, useState } from 'react';
import axios from 'axios';
import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from 'recharts';
import './App.css';

const chartColors = ['#0f766e', '#da7b4a', '#406a57', '#2f8f89', '#a85d3b', '#205f58'];

function App() {
  const [overview, setOverview] = useState(null);
  const [programs, setPrograms] = useState([]);
  const [filtersMeta, setFiltersMeta] = useState({ categories: [], locations: [], ranges: { maxCost: 0 } });
  const [filters, setFilters] = useState({
    programType: 'All',
    location: 'All',
    minOutcomeScore: 0,
    maxCost: '',
    minPeopleHelped: 0,
    search: ''
  });
  const [apiStatus, setApiStatus] = useState('Checking...');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');

  const apiBase = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';

  useEffect(() => {
    async function bootstrapDashboard() {
      try {
        const [healthRes, filtersRes] = await Promise.all([
          axios.get(`${apiBase}/api/health`),
          axios.get(`${apiBase}/api/filters`)
        ]);

        setApiStatus(healthRes.data.status === 'ok' ? 'Live' : 'Degraded');
        setFiltersMeta(filtersRes.data);
        setFilters((prev) => ({
          ...prev,
          maxCost: filtersRes.data?.ranges?.maxCost || ''
        }));
        setError('');
      } catch (requestError) {
        setApiStatus('Offline');
        setError('Unable to load live metrics. Start the backend on port 5000 and refresh.');
      }
    }

    bootstrapDashboard();
  }, [apiBase]);

  useEffect(() => {
    async function loadDashboardData() {
      if (apiStatus === 'Offline') {
        setIsLoading(false);
        return;
      }

      try {
        setIsLoading(true);
        const params = {
          ...filters
        };

        const [overviewRes, programsRes] = await Promise.all([
          axios.get(`${apiBase}/api/overview`, { params }),
          axios.get(`${apiBase}/api/programs`, { params })
        ]);

        setOverview(overviewRes.data);
        setPrograms(programsRes.data.programs || []);
        setError('');
      } catch (requestError) {
        setError('Unable to load filtered metrics. Please retry.');
      } finally {
        setIsLoading(false);
      }
    }

    loadDashboardData();
  }, [apiBase, filters, apiStatus]);

  function onFilterChange(event) {
    const { name, value } = event.target;
    setFilters((prev) => ({
      ...prev,
      [name]: name === 'minOutcomeScore' || name === 'maxCost' || name === 'minPeopleHelped'
        ? Number(value)
        : value
    }));
  }

  function resetFilters() {
    setFilters({
      programType: 'All',
      location: 'All',
      minOutcomeScore: 0,
      maxCost: filtersMeta?.ranges?.maxCost || 0,
      minPeopleHelped: 0,
      search: ''
    });
  }

  const topPrograms = useMemo(() => programs.slice(0, 3), [programs]);

  const typeChartData = useMemo(() => {
    const grouped = programs.reduce((acc, program) => {
      if (!acc[program.programType]) {
        acc[program.programType] = {
          programType: program.programType,
          avgImpact: 0,
          totalImpact: 0,
          count: 0
        };
      }

      acc[program.programType].totalImpact += program.impactScore;
      acc[program.programType].count += 1;
      acc[program.programType].avgImpact = Number(
        (acc[program.programType].totalImpact / acc[program.programType].count).toFixed(4)
      );

      return acc;
    }, {});

    return Object.values(grouped).sort((a, b) => b.avgImpact - a.avgImpact);
  }, [programs]);

  const locationChartData = useMemo(() => {
    const grouped = programs.reduce((acc, program) => {
      if (!acc[program.location]) {
        acc[program.location] = {
          name: program.location,
          peopleHelped: 0
        };
      }

      acc[program.location].peopleHelped += program.peopleHelped;
      return acc;
    }, {});

    return Object.values(grouped)
      .sort((a, b) => b.peopleHelped - a.peopleHelped)
      .slice(0, 6);
  }, [programs]);

  const metrics = overview?.metrics || {
    programsAnalyzed: 0,
    totalBudget: 0,
    totalPeopleHelped: 0,
    avgOutcomeScore: 0
  };

  const topProgram = overview?.topProgram;

  return (
    <div className="app-shell">
      <div className="bg-orb orb-left" />
      <div className="bg-orb orb-right" />

      <header className="hero">
        <p className="eyebrow">NGO IMPACT INTELLIGENCE</p>
        <h1>Turn Program Data Into Clear Funding Decisions</h1>
        <p className="hero-copy">
          A modern operations dashboard for NGOs to prioritize budgets, compare outcomes,
          and identify high-impact initiatives faster.
        </p>
        <div className="hero-meta">
          <span className={`status-pill ${apiStatus === 'Live' ? 'status-live' : 'status-offline'}`}>
            API: {apiStatus}
          </span>
          <span className="muted-chip">{isLoading ? 'Refreshing metrics...' : 'Metrics synced'}</span>
        </div>
      </header>

      {error && <p className="error-banner">{error}</p>}

      <section className="panel filters-panel">
        <div className="panel-heading">
          <p className="panel-label">Filter Controls</p>
          <button className="ghost-btn" type="button" onClick={resetFilters}>Reset</button>
        </div>
        <div className="filters-grid">
          <label>
            Program Type
            <select name="programType" value={filters.programType} onChange={onFilterChange}>
              <option value="All">All</option>
              {filtersMeta.categories.map((category) => (
                <option key={category} value={category}>{category}</option>
              ))}
            </select>
          </label>
          <label>
            Location
            <select name="location" value={filters.location} onChange={onFilterChange}>
              <option value="All">All</option>
              {filtersMeta.locations.map((location) => (
                <option key={location} value={location}>{location}</option>
              ))}
            </select>
          </label>
          <label>
            Min Outcome Score
            <input
              type="range"
              name="minOutcomeScore"
              min="0"
              max="10"
              step="0.1"
              value={filters.minOutcomeScore}
              onChange={onFilterChange}
            />
            <span className="range-value">{filters.minOutcomeScore}</span>
          </label>
          <label>
            Max Budget
            <input
              type="range"
              name="maxCost"
              min="1000"
              max={filtersMeta?.ranges?.maxCost || 200000}
              step="1000"
              value={filters.maxCost}
              onChange={onFilterChange}
            />
            <span className="range-value">${Number(filters.maxCost || 0).toLocaleString()}</span>
          </label>
          <label>
            Min People Helped
            <input
              type="number"
              name="minPeopleHelped"
              min="0"
              value={filters.minPeopleHelped}
              onChange={onFilterChange}
            />
          </label>
          <label>
            Search NGO
            <input
              type="text"
              name="search"
              value={filters.search}
              onChange={onFilterChange}
              placeholder="Search by NGO, location, or type"
            />
          </label>
        </div>
      </section>

      <section className="metrics-grid">
        <article className="metric-card">
          <p>Programs Analyzed</p>
          <h2>{metrics.programsAnalyzed}</h2>
        </article>
        <article className="metric-card">
          <p>Total Budget</p>
          <h2>${metrics.totalBudget.toLocaleString()}</h2>
        </article>
        <article className="metric-card">
          <p>People Reached</p>
          <h2>{metrics.totalPeopleHelped.toLocaleString()}</h2>
        </article>
        <article className="metric-card">
          <p>Average Outcome Score</p>
          <h2>{metrics.avgOutcomeScore}</h2>
        </article>
      </section>

      <section className="insights-layout">
        <article className="panel panel-featured">
          <p className="panel-label">Top Recommendation</p>
          {topProgram ? (
            <>
              <h3>{topProgram.ngoName}</h3>
              <p>
                {topProgram.programType} program with impact score{' '}
                <strong>{topProgram.impactScore}</strong>
              </p>
              <div className="mini-stats">
                <span>Budget: ${topProgram.cost.toLocaleString()}</span>
                <span>People Helped: {topProgram.peopleHelped}</span>
                <span>Outcome: {topProgram.outcomeScore}</span>
              </div>
            </>
          ) : (
            <p>No recommendation data available yet.</p>
          )}
        </article>

        <article className="panel">
          <p className="panel-label">High Impact Programs</p>
          <ul className="program-list">
            {topPrograms.map((program) => (
              <li key={program.id}>
                <div>
                  <h4>{program.ngoName}</h4>
                  <p>{program.programType}</p>
                </div>
                <span>{program.impactScore}</span>
              </li>
            ))}
          </ul>
        </article>
      </section>

      <section className="charts-grid">
        <article className="panel">
          <p className="panel-label">Impact By Program Type</p>
          <div className="chart-wrap">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={typeChartData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(10, 74, 69, 0.15)" />
                <XAxis dataKey="programType" tick={{ fontSize: 11 }} />
                <YAxis tick={{ fontSize: 11 }} />
                <Tooltip />
                <Bar dataKey="avgImpact" radius={[6, 6, 0, 0]}>
                  {typeChartData.map((entry, index) => (
                    <Cell key={`bar-${entry.programType}`} fill={chartColors[index % chartColors.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </article>

        <article className="panel">
          <p className="panel-label">People Reached By Location</p>
          <div className="chart-wrap">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={locationChartData}
                  cx="50%"
                  cy="50%"
                  outerRadius={88}
                  dataKey="peopleHelped"
                  labelLine={false}
                  label={({ name }) => name}
                >
                  {locationChartData.map((entry, index) => (
                    <Cell key={`cell-${entry.name}`} fill={chartColors[index % chartColors.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </article>
      </section>

      <footer className="page-footer">
        <p>Built for evidence-driven NGO planning and transparent impact reporting.</p>
      </footer>
    </div>
  );
}

export default App;
