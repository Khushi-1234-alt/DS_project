# utils.py
import re
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

from dotenv import load_dotenv
load_dotenv()

import os
import joblib
import openai
import numpy as np
import pandas as pd
import torch
import speech_recognition as sr
from transformers import pipeline
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

# 📂 Model loading with safe checks
MODEL_PATH = "models"
REQUIRED_MODELS = ["classifier.pkl", "regressor.pkl", "vectorizer.pkl"]

# Confirm working directory
print("🛠️ Current working directory:", os.getcwd())

# Load models safely
missing = [f for f in REQUIRED_MODELS if not os.path.exists(f"{MODEL_PATH}/{f}")]
if missing:
    raise FileNotFoundError(f"❌ Missing model files in /models/: {missing}")

clf = joblib.load(f"{MODEL_PATH}/classifier.pkl")
reg = joblib.load(f"{MODEL_PATH}/regressor.pkl")
vectorizer = joblib.load(f"{MODEL_PATH}/vectorizer.pkl")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in set(stopwords.words('english'))]
    return ' '.join(tokens)

# 🔐 OpenAI Key (replace or set in environment)
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

# 1. 🤖 GPT-based Support Response
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_gpt_response(prompt):
    try:
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Generate a polite support response: {prompt}"}]
        )
        return chat.choices[0].message.content
    except Exception as e:
        return f"⚠️ GPT error: {e}"



# 2. 🧠 Zero-Shot Classification
zero_classifier = pipeline("zero-shot-classification")
def zero_shot_classify(text, labels):
    res = zero_classifier(text, labels)
    return res['labels'][0]

# 3. ❤️ Sentiment Analysis
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

# 4. 🎙️ Speech-to-Text (Google STT)
def speech_to_text(file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)
