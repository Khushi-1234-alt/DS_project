# app.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Support Ticket Analyzer", layout="wide")

image = Image.open("assets/logo.png")
st.image(image, width=500)

st.title("📡 AI Support Ticket Analyzer")
st.markdown("""
Welcome to the **AI-powered dashboard** for customer support ticket management.

🔍 This app classifies ticket descriptions into issue categories and predicts estimated resolution times using Machine Learning.

Navigate using the sidebar to:
- Explore the data
- Predict new tickets
- View prediction history
- Learn more about the developer
""")
