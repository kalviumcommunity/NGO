# ---------------------------------------------------------
# IMPORT SECTION
# ---------------------------------------------------------
import math  # Even if minimal, standard practice puts imports at the top


# ---------------------------------------------------------
# FUNCTION DEFINITIONS
# ---------------------------------------------------------

def calculate_impact(people_helped, outcome_score, cost):
    """
    Calculates the impact score as reach * outcome divided by cost.
    Ensures logic is encapsulated for reuse across different datasets.
    """
    if cost <= 0:
        return 0.0
    
    impact_score = (people_helped * outcome_score) / cost
    return impact_score


def classify_program(impact_score):
    """
    Categorizes the impact score into meaningful levels for stakeholders.
    Centralizing this logic ensures consistency across reports.
    """
    if impact_score >= 0.05:
        return "High Impact"
    elif impact_score >= 0.02:
        return "Moderate Impact"
    else:
        return "Low Impact"


def display_summary(ngo_name, program_type, impact_score, classification):
    """
    Handles the presentation layer of the application.
    Separating output from computation makes the code cleaner.
    """
    print("=" * 60)
    print(f"NGO IMPACT SUMMARY: {ngo_name}")
    print(f"PROGRAM TYPE:       {program_type}")
    print("-" * 60)
    print(f"CALCULATED IMPACT:  {impact_score:.5f}")
    print(f"CLASSIFICATION:     {classification}")
    print("=" * 60)


# ---------------------------------------------------------
# MAIN EXECUTION BLOCK
# ---------------------------------------------------------

if __name__ == "__main__":
    # Defining sample NGO metrics for evaluation
    # We use descriptive snake_case names for all variables.
    organisation = "NGO Global Relief"
    sector = "Primary Education"
    reach = 850
    effectiveness = 0.88
    budget_used = 12000.00

    # Execute the structured data flow
    # Step 1: Computation
    score = calculate_impact(reach, effectiveness, budget_used)
    
    # Step 2: Categorization (reusing the score from Step 1)
    impact_level = classify_program(score)
    
    # Step 3: Reporting (passing all context and processed data)
    display_summary(organisation, sector, score, impact_level)

    print("\n[SUCCESS] Code structure demonstration complete.")
