# NGO Impact Optimizer - Loops Demonstration Script
# This script demonstrates iteration using for and while loops in Python.

# ---------------------------------------------------------
# 1. FOR LOOP (Iterating over a collection)
# ---------------------------------------------------------
print("--- 1. FOR LOOP DEMONSTRATION ---")

program_types = ["Education", "Healthcare", "Food Security", "Water Sanitation"]

print("Iterating through NGO program list:")
for program in program_types:
    print(f"- Processing Program Type: {program}")

print("\nIterating using range() to count programs:")
# range(start, stop)
for i in range(len(program_types)):
    print(f"Program #{i + 1}: {program_types[i]}")

print("-" * 50)

# ---------------------------------------------------------
# 2. WHILE LOOP (Conditional iteration)
# ---------------------------------------------------------
print("--- 2. WHILE LOOP DEMONSTRATION ---")

# Simulating processing a queue of NGO records
records_to_process = 5
processed_count = 0

print(f"Starting to process {records_to_process} records...")
while processed_count < records_to_process:
    processed_count += 1
    print(f"Iteration {processed_count}: Record processed successfully.")

print(f"Finished! Total records handled: {processed_count}")
print("-" * 50)

# ---------------------------------------------------------
# 3. LOOP CONTROL (Break and Continue)
# ---------------------------------------------------------
print("--- 3. LOOP CONTROL DEMONSTRATION ---")

# List of impact targets for different regions
impact_targets = [10, 15, 0, 25, 40, -5, 12]

print("Scanning impact targets list:")
for value in impact_targets:
    # Skip invalid data (continue)
    if value <= 0:
        print(f"  [SKIPPED] Found invalid target value: {value}")
        continue
    
    # Stop processing once a 'High Impact' target (>=40) is found (break)
    if value >= 40:
        print(f"  [STOPPED] High impact target found: {value}. Ending scan.")
        break
    
    print(f"  Processing valid target: {value}")

print("-" * 50)
print("Conclusion: Script executed successfully demonstrating loop usage and control.")
