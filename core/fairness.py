from utils.gemini_client import process_with_gemini

def evaluate_fairness(resume_text: str) -> dict:
    prompt = """
    Analyze the resume for potential demographic identifiers (e.g., gendered language, age indicators, cultural affiliations) and assess the risk of bias.
    
    Provide a JSON response with the following keys:
    - "demographic_indicators_found": List of detected potentially biasing terms (do not assume, only list facts).
    - "bias_risk_score": A score from 0 (Low Risk) to 100 (High Risk).
    - "recommendations": Suggestions to anonymize the text further or improve fairness-aware screening.
    """
    return process_with_gemini(prompt, resume_text)