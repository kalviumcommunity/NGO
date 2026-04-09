# NGO Impact Optimizer - Data Types Demonstration Script
# This script demonstrates usage of numeric and string data types in Python.

# ---------------------------------------------------------
# 1. Defining Variables
# ---------------------------------------------------------

# String variables (text data)
ngo_name = "NGO Global Relief"
program_type = "Medical Supplies Distribution"

# Numeric variables (Integer)
people_helped = 1200  # Number of people reached

# Numeric variables (Float)
outcome_score = 0.85  # Effectiveness score (0 to 1)
avg_cost_per_person = 12.50  # Cost in dollars

# Print initial types
print("--- Initial Types ---")
print(f"ngo_name type:           {type(ngo_name)}")
print(f"people_helped type:      {type(people_helped)}")
print(f"outcome_score type:      {type(outcome_score)}")
print("-" * 50)

# ---------------------------------------------------------
# 2. Arithmetic Operations
# ---------------------------------------------------------

# Calculate total impact (Numeric * Numeric)
total_impact = people_helped * outcome_score

# Calculate total cost
total_cost = people_helped * avg_cost_per_person

print("--- Arithmetic Operations ---")
print(f"Total Impact Score:      {total_impact:.2f}")
print(f"Total Operational Cost:  ${total_cost:,.2f}")
print("-" * 50)

# ---------------------------------------------------------
# 3. String Operations
# ---------------------------------------------------------

# Concatenation to form a message
program_info = ngo_name + " runs the " + program_type + " program."

# Using f-strings for clear output
summary_message = f"In the {program_type} program, {people_helped} people were assisted by {ngo_name}."

print("--- String Operations ---")
print(f"Concatenated Info:       {program_info}")
print(f"Formatted Summary:       {summary_message}")
print("-" * 50)

# ---------------------------------------------------------
# 4. Type Handling: Type Mismatch and Conversion
# ---------------------------------------------------------

print("--- Type Handling & Conversion ---")

# Example of a potential error:
# Trying to add a number to a string directly would cause a TypeError.
# Error: "NGO Name has helped " + people_helped
print("Handling type mismatch example:")

# Correct way: Explicit type conversion
try:
    # Attempting to demonstrate what happens if we don't convert (informative only, safe to run)
    error_trigger = "Number: " + str(people_helped) # Fixed here to prevent script crash
    print(f"Converted number to string for concatenation: {error_trigger}")
except TypeError:
    print("Caught a TypeError! Cannot add number directly to string.")

# Convert float to integer (truncation)
impact_as_int = int(total_impact)
print(f"Original impact (float): {total_impact:.2f}")
print(f"Converted impact (int):   {impact_as_int} (type: {type(impact_as_int)})")

# Convert integer to string for a specific message label
id_number = 101
id_label = "PROG-" + str(id_number)
print(f"Generated ID label:      {id_label}")

print("-" * 50)
print("Conclusion: Script executed successfully demonstrating data types and conversions.")
