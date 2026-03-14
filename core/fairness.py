from utils.gemini_client import process_with_gemini

def evaluate_fairness(resume_text: str) -> dict:
    prompt = """
    Analyze the resume for potential demographic identifiers (e.g., gendered language, age indicators, cultural affiliations) and assess the risk of bias.
    
    Provide a JSON response with the following keys:
    - "demographic_indicators_found": List of detected potentially biasing terms (do not assume, only list facts).
    - "bias_risk_score": A score from 0 (Low Risk) to 100 (High Risk).
    - "recommendations": List of actionable, personalized pieces of advice for the applicant on how they can improve their resume to catch the recruiter's attention and present their qualifications more effectively (while also mitigating any found demographic indicators).
    """
    return process_with_gemini(prompt, resume_text)