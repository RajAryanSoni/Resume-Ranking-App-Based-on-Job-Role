📄 Intelligent Resume Screening System with Bias Mitigation

Using Transformer-based Embeddings (BERT)

🔍 Project Overview

In modern recruitment systems, automated resume screening is widely used to handle large volumes of job applications. However, traditional systems often suffer from bias, keyword dependency, and lack of contextual understanding.

This project presents an Intelligent Resume Screening System that:

Uses pre-trained Transformer-based embeddings (BERT)

Performs semantic matching between resumes and job descriptions

Integrates bias mitigation techniques to promote fairness

Provides an interactive Streamlit web application for real-world usability

🎯 Objectives

Automate resume screening using context-aware NLP models

Rank resumes based on semantic similarity, not just keywords

Reduce bias related to:

Gender

Names

Age indicators

Provide a transparent, explainable, and ethical AI solution

Build a deployable ML application suitable for real-world hiring scenarios

🧠 Key Concepts Used

Transformer-based embeddings (BERT)

Cosine similarity for semantic ranking

Resume PDF parsing

Text preprocessing & normalization

Bias mitigation through sensitive attribute removal

Streamlit-based ML deployment

🏗️ System Architecture
User Uploads Resume (PDF)
          ↓
PDF Text Extraction
          ↓
Text Preprocessing
          ↓
Bias Mitigation Module
          ↓
BERT Embedding Generation
          ↓
Similarity Calculation
          ↓
Resume Ranking & Output

📁 Project Structure
Assignment Project/
│
├── app.py                 # Streamlit application
├── pdf_extractor.py       # Extracts text from PDF resumes
├── preprocessing.py       # Cleans and normalizes text
├── bias_mitigation.py     # Removes sensitive attributes
├── embedding.py           # Generates BERT embeddings
├── similarity.py          # Calculates similarity score
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignored files (__pycache__, etc.)

⚙️ Technologies Used
Category	Tools / Libraries
Programming	Python
NLP Model	BERT (Transformer-based embeddings)
ML Techniques	Cosine Similarity
PDF Handling	PyPDF2
Web App	Streamlit
Version Control	Git & GitHub
📥 Input & 📤 Output
Input

Resume(s) in PDF format

Job description (text input)

Output

Ranked resumes based on semantic similarity

Fairness-aware ranking after bias mitigation

Clear and interpretable matching scores

⚖️ Bias Mitigation Strategy

To promote ethical AI practices, the system removes or neutralizes:

Names

Gender-specific terms

Age indicators

Other sensitive attributes

This ensures that resumes are evaluated solely on skills, experience, and relevance, aligning with responsible AI principles.

🧪 How It Works (Pipeline Explanation)

PDF Extraction
Resume text is extracted using PDF parsing techniques.

Preprocessing

Lowercasing

Removing punctuation

Removing stopwords

Bias Mitigation
Sensitive terms are detected and removed.

Embedding Generation
Text is converted into numerical vectors using BERT embeddings.

Similarity Calculation
Cosine similarity is computed between resume embeddings and job description embeddings.

Ranking
Resumes are ranked based on similarity scores.

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Application
streamlit run app.py

3️⃣ Open Browser
http://localhost:8501

📊 Results & Observations

Improved matching accuracy compared to keyword-based systems

Reduced bias in resume evaluation

More fair and transparent ranking

Suitable for real-world recruitment scenarios

🔮 Future Enhancements

Multi-job role matching

Explainable AI (highlight matched skills)

Database integration

Multilingual resume support

Advanced bias detection using fairness metrics

📚 Academic Relevance

This project aligns with:

AI & ML coursework

Natural Language Processing

Ethical AI and Responsible ML

Real-world deployment of ML systems

👨‍🎓 Author

Raj Aryan
B.Tech (CSE – AI & ML)
GitHub: https://github.com/RajAryanSoni

📝 License

This project is intended for academic and educational purposes.