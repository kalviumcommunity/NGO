# NGO Impact Optimizer - Conditional Logic Demonstration Script
# This script demonstrates decision-making using if, elif, and else statements.

# ---------------------------------------------------------
# 1. Defining Sample Data
# ---------------------------------------------------------
ngo_name = "NGO Global Relief"
program_type = "Education"
cost = 5000
people_helped = 250
outcome_score = 0.82
impact_score = (people_helped * outcome_score) / cost  # Results in 0.041

print("-" * 50)
print(f"Program: {ngo_name} | Type: {program_type}")
print(f"Metrics: Cost={cost}, People={people_helped}, Outcome={outcome_score}")
print(f"Calculated Impact Score: {impact_score:.4f}")
print("-" * 50)

# ---------------------------------------------------------
# 2. Basic if Condition
# ---------------------------------------------------------
# Check if impact_score meets a minimum threshold for funding
threshold = 0.03
if impact_score > threshold:
    print("STATUS: High Impact Detected! Proceed with priority funding.")

# ---------------------------------------------------------
# 3. if-else Condition
# ---------------------------------------------------------
# Classify the program cost
if cost > 4000:
    print("BUDGET: High cost program - Requires senior management approval.")
else:
    print("BUDGET: Affordable program - Standard operational processing.")

# ---------------------------------------------------------
# 4. if-elif-else Condition
# ---------------------------------------------------------
# Classify effectiveness based on outcome_score
print("PERFORMANCE: ", end="")
if outcome_score >= 0.85:
    print("Highly Effective - Best in class results.")
elif outcome_score >= 0.7:
    print("Moderately Effective - Meeting institutional goals.")
else:
    print("Low Effectiveness - Review target metrics and delivery.")

# ---------------------------------------------------------
# 5. Logical Operators (and/or)
# ---------------------------------------------------------
# Combine multiple conditions for specific strategy checks
if program_type == "Education" and impact_score > 0.04:
    print("STRATEGY: Flagging as a 'High-Performing Education' model.")

if cost < 3000 or people_helped > 200:
    print("SCALABILITY: Program is either low cost or has high reach.")

# ---------------------------------------------------------
# 6. String Comparison
# ---------------------------------------------------------
# Comparing text data
if program_type != "Healthcare":
    print("NOTE: This is a non-healthcare initiative.")

if program_type.lower() == "education":
    print("VERIFIED: Program category confirmed as Education.")

print("-" * 50)
print("Conclusion: Script executed successfully demonstrating conditional logic.")
