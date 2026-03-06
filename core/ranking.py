from utils.gemini_client import process_with_gemini

def evaluate_resume(resume_text: str, job_description: str) -> dict:
    prompt = f"""
    Evaluate the resume against the following job description:
    {job_description}
    
    Provide a JSON response with the following keys:
    - "score": A score from 0 to 100 based on alignment.
    - "strengths": List of candidate's strong points.
    - "weaknesses": List of missing or weak skills.
    - "summary": A brief objective summary of the candidate's fit.
    """
    return process_with_gemini(prompt, resume_text)