import streamlit as st
import sqlite3
import pandas as pd

st.title("📁 Prediction History")

conn = sqlite3.connect("ticket_db.db")
df = pd.read_sql_query("SELECT * FROM complaints", conn)
conn.close()

if df.empty:
    st.warning("No prediction history found.")
else:
    st.dataframe(df)
