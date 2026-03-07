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