# NGO Impact Optimizer - Function Data Flow Demonstration Script
# This script demonstrates input, output, and data flow between functions.

# ---------------------------------------------------------
# 1. Function Definition: calculate_efficiency (Processing)
# ---------------------------------------------------------
def calculate_efficiency(cost, people_helped):
    """
    Calculates efficiency as people helped per unit of currency spent.
    
    Parameters:
    cost (float): Total budget spent.
    people_helped (int): Total number of people assisted.
    
    Returns:
    float: Efficiency value (people/unit cost).
    """
    # Defensive check to avoid division by zero
    if cost <= 0:
        return 0.0
        
    efficiency = people_helped / cost
    return efficiency

# ---------------------------------------------------------
# 2. Function Definition: format_output (Formatting)
# ---------------------------------------------------------
def format_output(efficiency_value):
    """
    Converts a numeric efficiency value into a human-readable status message.
    
    Parameters:
    efficiency_value (float): The calculated efficiency metric.
    
    Returns:
    str: A formatted descriptive string.
    """
    # We round the value for better presentation
    rounded_val = round(efficiency_value, 4)
    message = f"Analysis complete. The current efficiency rate is {rounded_val} people helped per dollar."
    return message

# ---------------------------------------------------------
# 3. Main Data Flow Execution
# ---------------------------------------------------------

# Sample Data
budget = 2000.0
reached = 450

print("-" * 50)
print(f"INPUT DATA: Budget=${budget}, People Reached={reached}")

# STEP A: Input parameters -> calculate_efficiency -> Return value
# The result of the processing is stored in a variable for reuse.
current_efficiency = calculate_efficiency(budget, reached)

# STEP B: Reuse the returned value in a condition
print(f"REUSE: Checking efficiency threshold...")
threshold = 0.2
if current_efficiency > threshold:
    status = "EXCEEDS TARGET"
else:
    status = "BELOW TARGET"
print(f"THRESHOLD CHECK: {status} (Target: {threshold})")

# STEP C: Pass the returned value into another function -> Return value
# Data flows from one function's output to another's input.
final_report = format_output(current_efficiency)

# STEP D: Final Output
print("-" * 50)
print(f"INTERNAL VALUE: {current_efficiency}")
print(f"FINAL OUTPUT:  {final_report}")
print("-" * 50)

print("Conclusion: Script executed successfully demonstrating function data flow.")
