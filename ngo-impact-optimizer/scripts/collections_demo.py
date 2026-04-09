# NGO Impact Optimizer - Python Collections Demonstration Script
# This script demonstrates the usage of Lists, Tuples, and Dictionaries.

# ---------------------------------------------------------
# 1. LISTS (Mutable Collection)
# ---------------------------------------------------------
print("--- 1. LIST DEMONSTRATION ---")

# Creating a list of NGO program types
program_types = ["Education", "Healthcare", "Food Security"]
print(f"Initial program types list: {program_types}")

# Accessing elements using index (0-based)
first_program = program_types[0]
print(f"First program in list (index 0): {first_program}")

# Modifying the list: Adding a new value
program_types.append("Water Sanitation")
print(f"List after adding a new program: {program_types}")

# Modifying the list: Updating an existing value
program_types[2] = "Nutrition & Food"
print(f"List after updating index 2: {program_types}")
print("-" * 50)

# ---------------------------------------------------------
# 2. TUPLES (Immutable Collection)
# ---------------------------------------------------------
print("--- 2. TUPLE DEMONSTRATION ---")

# Creating a tuple representing fixed NGO data (Name, Location)
# Tuples are used for data that should NOT change during execution.
ngo_info = ("NGO Global Relief", "Rural Sub-Sahara")
print(f"Fixed NGO information tuple: {ngo_info}")

# Accessing elements using index
name = ngo_info[0]
location = ngo_info[1]
print(f"Accessed from tuple: {name} located in {location}")

# Attempting to modify a tuple (Immutability Behavior)
# Uncommenting the line below would cause a TypeError: 'tuple' object does not support item assignment
# ngo_info[1] = "Urban Area" 

print("Note: Tuples are immutable. If you try to change ngo_info[1], it will raise a TypeError.")
print("-" * 50)

# ---------------------------------------------------------
# 3. DICTIONARIES (Key-Value Pair Collection)
# ---------------------------------------------------------
print("--- 3. DICTIONARY DEMONSTRATION ---")

# Creating a dictionary representing a single NGO program's metrics
current_program = {
    "ngo_name": "NGO Global Relief",
    "program_type": "Education",
    "cost": 5000,
    "people_helped": 200
}
print(f"Initial program dictionary: {current_program}")

# Accessing values using keys
impacted_people = current_program["people_helped"]
print(f"Accessed using key 'people_helped': {impacted_people}")

# Updating a value in the dictionary
current_program["people_helped"] = 250
print(f"Dictionary after updating 'people_helped': {current_program}")

# Adding a new key-value pair
current_program["outcome_score"] = 0.82
print(f"Dictionary after adding 'outcome_score': {current_program}")
print("-" * 50)

# ---------------------------------------------------------
# Summary of Differences
# ---------------------------------------------------------
print("--- COLLECTION SUMMARY ---")
print("LIST:       [] -> Indexed, Ordered, Mutable (Changeable)")
print("TUPLE:      () -> Indexed, Ordered, Immutable (Fixed)")
print("DICTIONARY: {} -> Key-Value Pairs, Unordered (pre-3.7), Mutable")
print("-" * 50)
