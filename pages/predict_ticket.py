import streamlit as st
import joblib
import re
import nltk
import sqlite3
from nltk.corpus import stopwords

# Setup
nltk.download('punkt')
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

# Load models
clf = joblib.load("models/classifier.pkl")
reg = joblib.load("models/regressor.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.title("🤖 Predict Ticket")

# Clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in STOPWORDS]
    return ' '.join(tokens)

# Save prediction to database
def log_prediction(text, category, days):
    conn = sqlite3.connect("ticket_db.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_text TEXT,
            predicted_category TEXT,
            predicted_time INTEGER
        )
    """)
    cursor.execute("""
        INSERT INTO complaints (ticket_text, predicted_category, predicted_time)
        VALUES (?, ?, ?)
    """, (text, category, int(days)))
    conn.commit()
    conn.close()

# Input + Prediction
text_input = st.text_area("📝 Enter support ticket description:")

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("Please enter a description before predicting.")
    else:
        cleaned = clean_text(text_input)
        vec = vectorizer.transform([cleaned])
        category = clf.predict(vec)[0]
        eta = reg.predict(vec)[0]

        st.success(f"Predicted Category: `{category}`")
        st.info(f"Estimated Resolution Time: **{round(eta, 2)} days**")

        log_prediction(text_input, category, eta)  # ⬅️ Log to DB

        st.success("✅ Your prediction has been saved to history.")
