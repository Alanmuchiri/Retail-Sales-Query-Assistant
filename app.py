import streamlit as st
import sqlite3
import google.generativeai as genai
from prompts import prompt
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

genai.configure(api_key=os.getenv("_GOOGLE_API_KEY")) 

def generate_sql(question):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    # Run query and load into dataframe
    df = pd.read_sql_query(sql, connection)
    connection.close()
    return df


st.set_page_config(
    page_title="AI Retail Data Analyst",
    page_icon="📊",
    layout="wide"
)

# Header Section
col1, col2 = st.columns([1,3])

with col1:
    st.image("images/logo.png", width=120)

with col2:
    st.title("AI Retail Data Analyst 📊")
    st.markdown(
        "Ask questions about **retail sales data** and the AI will generate SQL queries "
        "and retrieve insights from the database."
    )

st.divider()

# User Input
user_question = st.text_input(
    "💬 Ask a question about the sales data:",
    placeholder="Example: Which city generated the most revenue?"
)

# Analyze Button
if st.button("🔎 Analyze Data"):

    sql_query = generate_sql(user_question)

    st.subheader("🧠 Generated SQL Query")
    st.code(sql_query, language="sql")

    result = read_sql_query(sql_query, "data/sales.db")

    st.subheader("📊 Query Result")
    st.dataframe(result, use_container_width=True)

  