import sqlite3
import pandas as pd

conn = sqlite3.connect("MYSQL/mydatabase.db")

customer = pd.read_sql("""
SELECT * FROM Customer;
""",conn)

print(customer)
