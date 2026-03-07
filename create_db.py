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

sales_data = [
("Westlands","Nairobi","TV","Electronics",2,60000,120000,"2025-02-01"),
("Nyali","Mombasa","Fridge","Appliances",1,80000,80000,"2025-02-02"),
("Kisumu Central","Kisumu","Phone","Electronics",5,20000,100000,"2025-02-03"),
("CBD","Nairobi","Laptop","Electronics",3,90000,270000,"2025-02-04"),
("Nyali","Mombasa","Microwave","Appliances",2,15000,30000,"2025-02-05")
]

cursor.executemany("""
INSERT INTO SALES(branch,city,product,category,quantity,price,revenue,sale_date)
VALUES(?,?,?,?,?,?,?,?)
""", sales_data)

connection.commit()
connection.close()