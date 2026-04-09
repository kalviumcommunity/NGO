# NGO Impact Optimizer - Basic Data Analysis Script
# This script simulates a simple analysis task to identify high-impact NGO programs.

# Step 1: Define the dataset (small sample for demonstration)
# Each dictionary represents an NGO program with its resource usage and outcomes.
ngo_programs = [
    {
        "ngo_name": "NGO_A",
        "program_type": "Education",
        "cost": 5000,
        "people_helped": 200,
        "outcome_score": 0.8
    },
    {
        "ngo_name": "NGO_B",
        "program_type": "Healthcare",
        "cost": 8000,
        "people_helped": 150,
        "outcome_score": 0.9
    },
    {
        "ngo_name": "NGO_C",
        "program_type": "Food Security",
        "cost": 3000,
        "people_helped": 300,
        "outcome_score": 0.7
    },
    {
        "ngo_name": "NGO_D",
        "program_type": "Education",
        "cost": 7000,
        "people_helped": 180,
        "outcome_score": 0.85
    },
    {
        "ngo_name": "NGO_E",
        "program_type": "Healthcare",
        "cost": 6000,
        "people_helped": 220,
        "outcome_score": 0.75
    }
]

# Step 2: Perform data operations
# We calculate an "impact_score" for each program using the formula:
# impact_score = (people_helped * outcome_score) / cost
for program in ngo_programs:
    people_helped = program["people_helped"]
    outcome_score = program["outcome_score"]
    cost = program["cost"]
    
    # Calculate the score
    impact_score = (people_helped * outcome_score) / cost
    
    # Add the score to the program dictionary
    program["impact_score"] = impact_score

# Step 3: Print structured results
print("-" * 60)
print(f"{'NGO Name':<15} | {'Program Type':<15} | {'Impact Score':<10}")
print("-" * 60)

for program in ngo_programs:
    print(f"{program['ngo_name']:<15} | {program['program_type']:<15} | {program['impact_score']:<10.5f}")

print("-" * 60)

# Step 4: Identify and print the NGO with the highest impact score
highest_impact_ngo = ngo_programs[0]

for program in ngo_programs:
    if program["impact_score"] > highest_impact_ngo["impact_score"]:
        highest_impact_ngo = program

print(f"\nHighest Impact Program Analysis:")
print(f"NGO Name:       {highest_impact_ngo['ngo_name']}")
print(f"Program Type:   {highest_impact_ngo['program_type']}")
print(f"Impact Score:   {highest_impact_ngo['impact_score']:.5f}")
print("-" * 60)
