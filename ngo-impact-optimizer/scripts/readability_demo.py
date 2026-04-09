# NGO Impact Optimizer - Code Readability Demonstration
# This script illustrates how meaningful variable names and clear comments 
# improve code maintainability and understanding for data science projects.

# Initializing program metrics for a specific initiative
# We use descriptive snake_case names to ensure intent is clear at a glance.
ngo_name = "NGO Global Relief"
program_type = "Clean Water Access"
people_helped = 1500
outcome_score = 0.92  # Represents a 92% effectiveness or success rate
total_program_cost = 25000.00

# Calculating the impact score
# Purpose: This index helps prioritize funding by comparing reach/effectiveness against cost.
# Resulting score represents 'Impact Units' per dollar spent.
impact_score = (people_helped * outcome_score) / total_program_cost

# Displaying the program status report
# Descriptive wording in the final print ensures stakeholders understand the result.
print("-" * 60)
print(f"REPORT: {ngo_name} - {program_type}")
print(f"Reach: {people_helped} individuals | Effectiveness: {outcome_score * 100:.1f}%")
print(f"Funding Efficiency: ${total_program_cost:,.2f} invested")
print(f"Calculated Impact Score: {impact_score:.5f}")
print("-" * 60)

# Conclusion: Using clear variables like 'people_helped' instead of abbreviations 
# like 'ph' makes the arithmetic logic self-documenting.
