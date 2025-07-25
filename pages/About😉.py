# pages/4_About.py
import streamlit as st

st.title("👩‍💻 About Us")

st.markdown("""
🧠 AI-Powered Smart Dashboard for Support Ticket Management
This AI-powered dashboard system is designed to automate, analyze, and enhance customer support operations by leveraging the capabilities of Natural Language Processing (NLP) and Machine Learning (ML). The goal is to create a smart, interactive, and self-improving solution that streamlines ticket classification, response estimation, and feedback integration—improving both efficiency and customer satisfaction.


🚀 Key Features:

🔍 Ticket Classification: Automatically categorizes customer complaints into labels such as billing, technical issues, refunds, login errors, etc. using a trained Multinomial Naive Bayes classifier on TF-IDF features.

⏱️ Resolution Time Estimation: Utilizes Linear Regression to predict the expected resolution time (in days) for a given support ticket, allowing for better resource planning and transparency.

💬 Feedback Loop: Collects user-submitted feedback and complaint ratings which are stored in a SQLite database, helping to retrain and refine the models based on real-world corrections.

📊 Historical Tracking: Visualizes ticket history and classification outcomes in an easy-to-navigate table view for admins.

🎙️ Speech-to-Text Conversion: Converts audio complaints (in WAV or MP3) to text using libraries like SpeechRecognition, adding multimodal input support.

🧠 Sentiment Analysis: Identifies customer sentiment (positive/neutral/negative) using VADER Sentiment Analyzer, providing emotional insight into the complaints.

🧪 Zero-Shot Classification: Applies transformer-based NLP models from HuggingFace to classify text into arbitrary user-defined categories, showcasing flexible AI reasoning.

🤖 GPT-Powered Auto Response: Generates AI-written, context-aware responses to tickets using OpenAI's GPT-based text generation, simulating intelligent replies.


🛠️ Technologies & Tools Used:

Area	Stack / Tools
Frontend	Streamlit, HTML, CSS
Backend	Flask (for dashboard version), SQLite3
ML Models	Multinomial Naive Bayes (classification), Linear Regression (time prediction), Transformers (zero-shot)
NLP Preprocessing	spaCy, NLTK (tokenization, stopword removal, lemmatization)
Model Explanation	(Optional) SHAP for interpretability
Visualization	Streamlit Components, Tables
Storage	Local SQLite database for storing tickets and feedback
Extras	SpeechRecognition, OpenAI GPT (via API), Joblib for model serialization


🔍 Workflow Overview:

Data Preprocessing: Clean and prepare historical ticket data using NLP techniques (tokenization, TF-IDF, etc.).

Model Training: Train classification and regression models using scikit-learn.

UI Integration: Deploy models via Streamlit for real-time inference and interaction.

Feedback Handling: Store new ticket data and user feedback into the database.

Optional SHAP Interpretation: Explain ML decisions (removed in lightweight mode if needed).

Interactive Navigation: Sidebar-driven app layout for seamless access to modules.


👩‍💻 Developer Info:

Name: Khushi Gupta

Background: Final-year Computer Science undergraduate specializing in Data Science, AI, and Full-Stack ML Applications.

Project Goal: To integrate core machine learning concepts with real-world application design, transforming traditional customer service platforms into intelligent systems.

🎯 Capstone Objectives:

Bridge the gap between raw ticket logs and intelligent automation.

Showcase an end-to-end AI product development lifecycle.

Enhance user experience while maintaining explainability and control.

Make the system adaptable across domains like e-commerce, telecom, healthcare, and EdTech.


💡 Ready for Collaboration!

For improvements, research collaborations, internships, or project extensions (e.g., cloud deployment, continuous learning), feel free to connect.
""")
