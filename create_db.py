import sqlite3

connection = sqlite3.connect("data/sales.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE SALES(
id INTEGER PRIMARY KEY AUTOINCREMENT,
branch TEXT,
city TEXT,
product TEXT,
category TEXT,
quantity INT,
price REAL,
revenue REAL,
sale_date TEXT
)
""")