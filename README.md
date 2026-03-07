# AI Retail Data Analyst (Natural Language to SQL)

An **AI-powered data analytics assistant** that allows users to query retail sales data using **natural language**. The system converts user questions into **SQL queries using Google's Gemini LLM** and retrieves insights from a **SQLite database**.

This project demonstrates how **Large Language Models (LLMs)** can be integrated with **databases and analytics workflows** to simplify data exploration.

---

## Project Overview

In many companies, managers and non-technical staff need insights from databases but **do not know SQL**.

This project solves that problem by allowing users to:

1. Ask questions in **plain English**
2. Automatically generate **SQL queries using AI**
3. Execute the query on a **sales database**
4. Display the **results in a web interface**

**Example:**

User Question:
```
Which city generated the highest revenue?
```

AI Generated SQL:
```sql
SELECT city, SUM(revenue)
FROM SALES
GROUP BY city
ORDER BY SUM(revenue) DESC
LIMIT 1;
```

Result:
```
Nairobi — 390000
```

---

## Key Features

- Natural Language → SQL conversion using **Gemini LLM**
- Interactive **Streamlit dashboard**
- Lightweight **SQLite database**
- Prompt engineering for structured SQL generation
- Business-focused dataset based on **retail sales**
- Clean and modular project structure

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web interface |
| SQLite | Local database |
| Google Gemini API | Natural language to SQL generation |
| dotenv | Secure API key management |
| Git & GitHub | Version control |

---

## Project Structure

```
ai-retail-data-analyst/
│
├── app.py                # Streamlit web application
├── create_db.py          # Script to create and populate database
├── prompts.py            # LLM prompt instructions
├── requirements.txt      # Project dependencies
├── .env                  # API key configuration
│
├── data/
│   └── sales.db          # SQLite database
│
├── images/
│   └── logo.png          # App logo
│
└── README.md
```

---

## Database Schema

**Table: SALES**

| Column | Description |
|---|---|
| id | Unique sale identifier |
| branch | Store branch |
| city | City where sale occurred |
| product | Product name |
| category | Product category |
| quantity | Units sold |
| price | Price per unit |
| revenue | Total revenue from sale |
| sale_date | Date of transaction |

**Example Records:**

| branch | city | product | revenue |
|---|---|---|---|
| Westlands | Nairobi | TV | 120000 |
| Nyali | Mombasa | Fridge | 80000 |

---

## Example Questions the System Can Answer

```
Show sales in Nairobi
```
```
Which product generated the highest revenue?
```
```
What is the total revenue?
```
```
Which city sells the most electronics?
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-retail-data-analyst.git
cd ai-retail-data-analyst
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Gemini API Key

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

> You can get a key from: https://ai.google.dev/

### 5. Create the Database

```bash
python create_db.py
```

### 6. Run the Application

```bash
streamlit run app.py
```

---

## Example Workflow

1. User enters a question in the Streamlit interface.
2. The question is sent to the Gemini API.
3. Gemini generates the corresponding SQL query.
4. The query is executed on the SQLite database.
5. Results are returned and displayed to the user.

**Example:**

User Input:
```
Which city generated the most revenue?
```

Generated SQL:
```sql
SELECT city, SUM(revenue)
FROM SALES
GROUP BY city
ORDER BY SUM(revenue) DESC
LIMIT 1;
```

Result:
```
Nairobi - 390000
```

---

## Skills Demonstrated

- Natural Language Processing with LLMs
- Prompt Engineering
- SQL query generation
- Database querying and management
- Python backend development
- API integration
- Data application development with Streamlit
- Version control with Git

---

## Future Improvements

- Support for **multiple tables**
- Data visualization dashboards
- Upload custom datasets
- Query validation and security checks
- Integration with **PostgreSQL or cloud databases**
- Conversational chat interface

---

## Author

**Alan Muchiri**

Mechatronics Engineer transitioning into **Data Engineering and AI Systems**.

**Skills:** Python · SQL · Data Engineering · IoT Systems · AI Integration · Automation Systems

---

## License

This project is licensed under the **MIT License**.
