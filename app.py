import streamlit as st
import sqlite3
import google.generativeai as genai
from prompts import prompt
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_sql(question):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content([prompt[0],question])
    return response.text

def run_query(sql):
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

st.title("AI Retail Data Analyst")

question = st.text_input("Ask a question about sales data")

if st.button("Analyze"):
    sql_query = generate_sql(question)

    st.subheader("Generated SQL")
    st.code(sql_query)

    result = run_query(sql_query)

    st.subheader("Results")
    st.write(result)