# app.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI SMART COMPLAINT TIME PREDICTOR", layout="wide")


st.title("📡 AI Support Ticket Analyzer")
st.markdown("""
Welcome to the AI-Powered Support Ticket Management Dashboard

In today's fast-paced digital environment, managing customer complaints and support tickets efficiently is crucial for ensuring high customer satisfaction and operational excellence. This intelligent system leverages Artificial Intelligence (AI) and Machine Learning (ML) to automate and enhance the entire support process.

🔍 Key Functionalities:
Automated Ticket Classification: Using Natural Language Processing (NLP), the system analyzes the text of incoming complaints and classifies them into predefined categories such as technical issues, billing, refunds, service delays, and more.

Resolution Time Prediction: A regression-based ML model predicts the estimated resolution time based on historical patterns, ticket content, and priority levels—helping support teams plan resources better and manage expectations.

Sentiment Analysis & Add-ons: Additional AI features such as sentiment detection and zero-shot classification provide deeper insights into customer emotions and complaint context.

Speech-to-Text: Converts spoken complaints into readable text, enabling multi-format complaint handling for increased accessibility.

Interactive Dashboard: A user-friendly web interface built with Flask and Streamlit allows admins to explore ticket data, track history, manage feedback, and monitor performance—all in one place.

Feedback Loop & Retraining: User-submitted feedback helps validate predictions and supports continuous model retraining, improving accuracy over time.

🧭 How to Navigate:

Use the sidebar to access:

📂 Explore Data – View and analyze past complaints, categories, and resolution metrics.

🔮 Predict New Tickets – Input new complaint text to receive instant classification and resolution estimation.

📝 Feedback & Correction – Submit corrections or feedback to enhance system learning.

🧠 AI Add-ons – Try tools like GPT response generation, sentiment scoring, and speech recognition.

👤 About the Developer – Learn more about the creator and the vision behind this project.
""")
