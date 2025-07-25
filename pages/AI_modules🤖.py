# pages/AI_modules.py
import streamlit as st
from utils import *

st.set_page_config(page_title="AI Add-ons", layout="wide")
st.title("🧠 Advanced AI Modules")

# 🎯 Select Module
tabs = st.tabs(["🤖 GPT Response", "🧠 Zero-Shot Classification",  "❤️ Sentiment", "🎙️ Speech-to-Text"])

# 1. GPT Auto-Responder
with tabs[0]:
    st.subheader("🤖 GPT Auto-Response Generator")
    prompt = st.text_area("Enter a customer ticket:")
    if st.button("Generate Response"):
        response = generate_gpt_response(prompt)
        st.success(response)

# 2. Zero-Shot Classification
with tabs[1]:
    st.subheader("🧠 Zero-Shot Text Classifier")
    input_text = st.text_area("Enter a ticket description:", key="zsc_text")
    candidate_labels = st.text_input("Enter labels separated by commas:", value="billing,technical,refund")
    if st.button("Classify", key="zsc_btn"):
        label = zero_shot_classify(input_text, candidate_labels.split(","))
        st.info(f"Predicted Label: {label}")

# 3. Sentiment Analysis
with tabs[2]:
    st.subheader("❤️ Sentiment Analyzer")
    text = st.text_area("Enter text to analyze:", key="sentiment_text")
    if st.button("Analyze Sentiment"):
        score = analyze_sentiment(text)
        st.write(f"Sentiment Score: {score:.2f}")

# 4. Speech to Text
with tabs[3]:
    st.subheader("🎙️ Speech to Text")
    audio_file = st.file_uploader("Upload a WAV/MP3 file", type=["wav", "mp3"])
    if st.button("Transcribe"):
        if audio_file:
            result = speech_to_text(audio_file)
            st.text_area("Transcription Result:", value=result, height=150)
        else:
            st.warning("Please upload a file first.")
