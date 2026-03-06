import os
import streamlit as st

def get_gemini_api_key():
    if "GEMINI_API_KEY" in st.secrets:
        return st.secrets["GEMINI_API_KEY"]
    return os.environ.get("GEMINI_API_KEY")

SYSTEM_PROMPT = """You are an objective, fairness-aware AI Resume Screening Agent. 
Evaluate the candidate based strictly on skills, experience, and qualifications. 
Ignore demographic identifiers."""