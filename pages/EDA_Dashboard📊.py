# # pages/1_EDA_Dashboard.py
# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# st.title("📊 EDA Dashboard")
# df = pd.read_csv("customer_support_tickets.csv")

# st.header("Dataset Overview")
# st.dataframe(df.head())

# st.subheader("Ticket Type Frequency")
# fig, ax = plt.subplots()
# sns.countplot(y=df['Ticket Type'], order=df['Ticket Type'].value_counts().index, ax=ax)
# st.pyplot(fig)

# st.subheader("Resolution Time Distribution")
# fig, ax = plt.subplots()
# sns.histplot(df['Time to Resolution'], bins=30, kde=True, ax=ax)
# st.pyplot(fig)

# st.subheader("Word Cloud of Descriptions")
# wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(df['Ticket Description'].astype(str)))
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.imshow(wordcloud, interpolation='bilinear')
# ax.axis("off")
# st.pyplot(fig)
# pages/1_EDA_Dashboard.py
# pages/1_EDA_Dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.ticker as mtick

# Set Streamlit config
st.set_page_config(page_title="Customer Support EDA", layout="wide")
st.title("📊 Customer Support Ticket Dashboard")

# Load and preprocess
df = pd.read_csv("customer_support_tickets.csv")

df['Time to Resolution'] = pd.to_numeric(df['Time to Resolution'], errors='coerce')
df['Customer Satisfaction Rating'] = pd.to_numeric(df['Customer Satisfaction Rating'], errors='coerce')
df['Ticket Description'] = df['Ticket Description'].fillna("")
df['Date of Purchase'] = pd.to_datetime(df['Date of Purchase'], errors='coerce')

# Derived columns
df['Month'] = df['Date of Purchase'].dt.to_period('M')

# === SECTION 1: DATAFRAME OVERVIEW ===
st.header("🗂 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# === SECTION 2: FIRST ROW OF CHARTS ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎟️ Ticket Type Frequency")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(y='Ticket Type', data=df, order=df['Ticket Type'].value_counts().index, palette='viridis', ax=ax)
    ax.set_title("Ticket Types", fontsize=12)
    st.pyplot(fig)

with col2:
    st.subheader("📌 Ticket Status Distribution")
    status_counts = df['Ticket Status'].value_counts()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
    ax.axis('equal')
    st.pyplot(fig)

# === SECTION 3: SECOND ROW OF CHARTS ===
col3, col4 = st.columns(2)

with col3:
    st.subheader("⏱️ Resolution Time Distribution")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(df['Time to Resolution'].dropna(), bins=30, kde=True, color='steelblue', ax=ax)
    ax.set_title("Time to Resolution", fontsize=12)
    st.pyplot(fig)

with col4:
    st.subheader("⭐ Satisfaction by Ticket Priority")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(x='Ticket Priority', y='Customer Satisfaction Rating', data=df, palette='coolwarm', ax=ax)
    ax.set_title("Satisfaction by Priority", fontsize=12)
    st.pyplot(fig)

# === SECTION 4: THIRD ROW OF CHARTS ===
col5, col6 = st.columns(2)

with col5:
    st.subheader("📞 Ticket Channel Usage")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(data=df, x='Ticket Channel', order=df['Ticket Channel'].value_counts().index, palette='mako', ax=ax)
    ax.set_title("Ticket Channels", fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
    st.pyplot(fig)

with col6:
    st.subheader("🧑‍🤝‍🧑 Age Distribution by Gender")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.violinplot(x='Customer Gender', y='Customer Age', data=df, palette='Set3', ax=ax)
    ax.set_title("Customer Age by Gender", fontsize=12)
    st.pyplot(fig)

# === SECTION 5: LINE CHART & WORD CLOUD ===
st.subheader("📅 Monthly Ticket Volume")
monthly_tickets = df['Month'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 4))
monthly_tickets.plot(kind='line', marker='o', color='orange', ax=ax)
ax.set_title("Tickets per Month", fontsize=12)
ax.set_ylabel("Ticket Count")
ax.set_xlabel("Month")
st.pyplot(fig)

st.subheader("☁️ Word Cloud of Ticket Descriptions")
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Dark2').generate(" ".join(df['Ticket Description']))
fig, ax = plt.subplots(figsize=(10, 4))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

