# Ethical Impact Assessment Report: AI Resume Screening Agent

## 1. Purpose and Scope
This system automates initial resume screening by evaluating candidate skills against job descriptions. It incorporates a parallel fairness evaluation to detect and flag potential demographic biases.

## 2. Potential Biases Identified
* **Proxy Variables:** Educational institutions, zip codes, or extracurricular affiliations may act as proxies for race or socioeconomic status.
* **Language Bias:** System may favor resumes written with normative corporate phrasing over those from neurodivergent candidates or non-native speakers.
* **Historical Bias:** LLM training data may inadvertently score historically male-dominated experience profiles higher in technical roles.

## 3. Mitigation Strategies (Fairness-Aware Improvements)
* **Pre-processing Anonymization:** Implement Named Entity Recognition (NER) to redact names, dates, and locations before feeding text to the ranking prompt.
* **Strict Prompt Engineering:** The `SYSTEM_PROMPT` explicitly forces the model to ignore demographic identifiers and focus purely on skills.
* **Dual-Processing Architecture:** Separating the ranking logic (`ranking.py`) from the bias detection (`fairness.py`) ensures transparency in *why* a resume received its score.

## 4. Human-in-the-Loop Integration
This tool is designed as an *assistive* screener. Candidates scoring below the threshold or those flagging a high 'Bias Risk Score' must undergo manual review by a human HR representative.