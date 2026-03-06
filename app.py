import streamlit as st
from utils.file_processor import extract_text
from utils.gemini_client import initialize_gemini
from utils.anonymizer import anonymize_text
from core.ranking import evaluate_resume
from core.fairness import evaluate_fairness

st.set_page_config(page_title="AI Resume Screener", layout="wide")

try:
    initialize_gemini()
except ValueError as e:
    st.error(str(e))
    st.stop()

st.title("AI Resume Screening & Fairness Agent")

job_description = st.text_area("Enter Job Description", height=150)
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if st.button("Analyze Resume") and uploaded_file and job_description:
    with st.spinner("Extracting and Anonymizing text..."):
        try:
            raw_resume_text = extract_text(uploaded_file)
            # Apply Anonymization Before LLM Processing
            safe_resume_text = anonymize_text(raw_resume_text)
        except Exception as e:
            st.error(f"Error processing file: {e}")
            st.stop()

    with st.expander("View Anonymized Resume Text (For Verification)"):
        st.write(safe_resume_text)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Ranking Logic")
        with st.spinner("Evaluating qualifications..."):
            # Pass the SAFE text to the ranking evaluator
            evaluation = evaluate_resume(safe_resume_text, job_description)
            if "error" in evaluation:
                st.error(evaluation["error"])
            else:
                st.metric(label="Match Score", value=f"{evaluation.get('score', 0)}/100")
                st.write("**Strengths:**", ", ".join(evaluation.get('strengths', [])))
                st.write("**Weaknesses:**", ", ".join(evaluation.get('weaknesses', [])))
                st.info(evaluation.get('summary', ''))

    with col2:
        st.subheader("Fairness Evaluation")
        with st.spinner("Analyzing for remaining bias indicators..."):
            # Pass the RAW text to evaluate_fairness to see what the anonymizer missed or what structural bias exists
            fairness = evaluate_fairness(raw_resume_text)
            if "error" in fairness:
                st.error(fairness["error"])
            else:
                st.metric(label="Bias Risk Score", value=f"{fairness.get('bias_risk_score', 0)}/100")
                st.write("**Detected Indicators:**", ", ".join(fairness.get('demographic_indicators_found', [])))
                st.write("**Improvement Recommendations:**")
                for rec in fairness.get('recommendations', []):
                    st.write(f"- {rec}")