import os
import streamlit as st

def get_gemini_api_key():
    import tomllib
    
    # Try environment variable first
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return api_key
        
    # Fallback to secrets.toml
    secrets_path = os.path.join(os.path.dirname(__file__), ".streamlit", "secrets.toml")
    if os.path.exists(secrets_path):
        try:
            with open(secrets_path, "rb") as f:
                secrets = tomllib.load(f)
                return secrets.get("GEMINI_API_KEY")
        except Exception as e:
            print(f"Error reading secrets.toml: {e}")
            
    return None

SYSTEM_PROMPT = """You are an objective, fairness-aware AI Resume Screening Agent. 
Evaluate the candidate based strictly on skills, experience, and qualifications. 
Ignore demographic identifiers."""