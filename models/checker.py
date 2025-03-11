# importing necessary libraries
from rapidfuzz import fuzz
from app.criteria import CRITERIA

def check_visa_eligibility(text):
    
    matched_criteria = {}

    # fuzzy matching threshold 
    threshold = 85

    # criteria and keywords evaluation
    for criterion, keywords in CRITERIA.items():
        match_count = 0

        # checking for fuzzy matches 
        for keyword in keywords:
            similarity_score = fuzz.partial_ratio(keyword.lower(), text.lower())
            if similarity_score >= threshold:
                match_count += 1

        if match_count > 0: # at least have 1 fuzzy match
            matched_criteria[criterion] = match_count   # add matches to the output for each criterion

    total_matched_criteria = len(matched_criteria)

    # rating based on the number of matched criteria
    if total_matched_criteria >= 6:
        rating = "High"
    elif 3 <= total_matched_criteria < 6:
        rating = "Medium"
    else:
        rating = "Low"

    # returning matched criteria and rating as the final response
    return {
        "matched_criteria": matched_criteria,
        "rating": rating
    }
