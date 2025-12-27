import streamlit as st
import pandas as pd

from preprocessing import clean_text
from bias_mitigation import remove_bias
from embedding import get_embedding
from similarity import compute_similarity
from pdf_extractor import extract_text_from_pdf

st.set_page_config(
    page_title="Intelligent Resume Screening System",
    layout="wide"
)

st.title("📄 Intelligent Resume Screening System")
st.subheader("Using BERT, Transformers & Bias Mitigation")

# =============================
# JOB DESCRIPTION INPUT
# =============================
st.sidebar.header("📌 Job Description")
job_description = st.sidebar.text_area(
    "Enter Job Description",
    height=200,
    placeholder="Looking for a candidate skilled in Python, Machine Learning, NLP, BERT..."
)

# =============================
# PDF UPLOAD
# =============================
st.sidebar.header("📤 Upload Resume PDFs")
uploaded_files = st.sidebar.file_uploader(
    "Upload one or more resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# =============================
# SCREEN BUTTON
# =============================
if st.sidebar.button("🔍 Screen Resumes"):

    if job_description.strip() == "":
        st.warning("⚠️ Please enter a Job Description")
    
    elif not uploaded_files:
        st.warning("⚠️ Please upload at least one resume PDF")

    else:
        st.info("🔄 Processing resumes... Please wait")

        # Process Job Description
        jd_clean = clean_text(job_description)
        jd_clean = remove_bias(jd_clean)
        jd_embedding = get_embedding(jd_clean)

        results = []

        for pdf in uploaded_files:
            resume_text = extract_text_from_pdf(pdf)

            resume_text = clean_text(resume_text)
            resume_text = remove_bias(resume_text)

            resume_embedding = get_embedding(resume_text)
            score = compute_similarity(resume_embedding, jd_embedding)

            results.append({
                "Resume File": pdf.name,
                "Match Score (%)": round(score * 100, 2)
            })

        results_df = pd.DataFrame(results)
        results_df = results_df.sort_values(
            by="Match Score (%)",
            ascending=False
        )

        st.success("✅ Resume Screening Completed")

        st.subheader("📊 Ranked Candidates")
        st.dataframe(results_df, use_container_width=True)

        st.markdown("---")
        st.subheader("🛡️ Bias Mitigation Applied")
        st.markdown("""
        ✔ Gender indicators removed  
        ✔ Name-based bias minimized  
        ✔ Age-related data ignored  
        ✔ College reputation excluded  
        ✔ Ranking based **only on skills & experience**
        """)
