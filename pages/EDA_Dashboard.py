# pages/1_EDA_Dashboard.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("📊 EDA Dashboard")
df = pd.read_csv("customer_support_tickets.csv")

st.header("Dataset Overview")
st.dataframe(df.head())

st.subheader("Ticket Type Frequency")
fig, ax = plt.subplots()
sns.countplot(y=df['Ticket Type'], order=df['Ticket Type'].value_counts().index, ax=ax)
st.pyplot(fig)

st.subheader("Resolution Time Distribution")
fig, ax = plt.subplots()
sns.histplot(df['Time to Resolution'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Word Cloud of Descriptions")
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(df['Ticket Description'].astype(str)))
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
