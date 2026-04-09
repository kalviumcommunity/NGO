# NGO Impact Optimizer - Functions Demonstration Script
# This script demonstrates how to define and use functions to organize reusable logic.

# ---------------------------------------------------------
# 1. Function Definition: calculate_impact
# ---------------------------------------------------------
def calculate_impact(people_helped, outcome_score, cost):
    """
    Calculates the impact score of an NGO program based on reach, 
    effectiveness, and cost efficiency.
    
    Parameters:
    people_helped (int): Number of individuals assisted.
    outcome_score (float): Effectiveness rating (0.0 to 1.0).
    cost (float): Total operational cost of the program.
    
    Returns:
    float: The calculated impact score.
    """
    if cost <= 0:
        return 0.0  # Prevent division by zero
        
    impact_score = (people_helped * outcome_score) / cost
    return impact_score

# ---------------------------------------------------------
# 2. Function Definition: display_program_info
# ---------------------------------------------------------
def display_program_info(ngo_name, program_type, impact_score):
    """
    Prints a formatted report summarizing the NGO program's impact.
    
    Parameters:
    ngo_name (str): The name of the NGO.
    program_type (str): The category of the program.
    impact_score (float): The pre-calculated impact metric.
    """
    print("-" * 50)
    print(f"REPORT: {ngo_name}")
    print(f"CATEGORY: {program_type}")
    print(f"ANALYSIS: This program has an impact score of {impact_score:.4f}.")
    
    if impact_score > 0.03:
        print("RECOMMENDATION: High impact observed. Consider scaling this model.")
    else:
        print("RECOMMENDATION: Standard impact. Review for potential optimizations.")
    print("-" * 50)

# ---------------------------------------------------------
# 3. Main Execution and Function Usage
# ---------------------------------------------------------

# Sample NGO Data
name = "NGO Global Relief"
category = "Medical Supplies Distribution"
helped = 1200
score = 0.85
budget = 15000.0

print("Executing analysis for NGO database...")

# Step A: Call calculate_impact and store the returned value
calculated_score = calculate_impact(helped, score, budget)
print(f"DEBUG: Internal calculation returned: {calculated_score}")

# Step B: Pass the result into display_program_info
display_program_info(name, category, calculated_score)

print("Conclusion: Script executed successfully demonstrating function modularity.")
