import sqlite3

import pandas as pd

conn = sqlite3.connect('MYSQL/cities.db')

conn.execute("DROP TABLE IF EXISTS City;")

conn.execute("""

CREATE TABLE City (

City_Id INTEGER PRIMARY KEY,

City_Name TEXT NOT NULL UNIQUE,

Country TEXT NOT NULL,

Population INTEGER,

Is_Capital TEXT DEFAULT 'No'

);

""")

conn.commit()

print("Table created successfully!")

# ---- PART 2: INSERT — Adding Rows to the Table ----

# INSERT INTO adds one row at a time.

# Every NOT NULL column must receive a value.

# Columns with a DEFAULT can be left out — the default fills in.

# conn.commit() saves all inserts permanently.

conn.execute("INSERT INTO City VALUES (1, 'Tokyo', 'Japan', 13960000, 'Yes');")

conn.execute("INSERT INTO City VALUES (2, 'Nairobi', 'Kenya', 4397000, 'Yes');")

conn.execute("INSERT INTO City VALUES (3, 'Mumbai', 'India', 20667656, 'No');")

conn.execute("INSERT INTO City VALUES (4, 'Sao Paulo', 'Brazil', 12325232, 'No');")

conn.execute("INSERT INTO City VALUES (5, 'London', 'UK', 9541000, 'Yes');")

conn.execute("INSERT INTO City (City_Id, City_Name, Country) VALUES (6, 'Sydney', 'Australia');")

conn.commit()

print("Rows inserted successfully!")

cities = pd.read_sql("SELECT * FROM City;", conn)

print(cities)


try:
    conn.execute("INSERT INTO City VALUES(1, 'Lahore','Pakistan','8755789','Yes')")
    conn.commit


except Exception as e:
    conn.rollback()
    print("rejected",e)
    print("DUPLICATE NOT ALLOWED")


try:
    conn.execute("INSERT INTO City VALUES(755, 'Sahiwal',NULL,'876589','YES')")
    conn.commit()


except Exception as e:
    conn.rollback()
    print("rejected",e)
    print("DUPLICATE NOT ALLOWED")

try:
    conn.execute("INSERT INTO City VALUES(755, 'Tokyo','pakistan','876589','YES')")
    conn.commit()


except Exception as e:
    conn.rollback()
    print("rejected",e)
    print("DUPLICATE NOT ALLOWED")




    



print1 = pd.read_sql("""SELECT * FROM City
WHERE City_Name = 'Sydney'
""",conn)

print(print1)




print2 = pd.read_sql("""SELECT City_Name,Population FROM City

""",conn)

print(print2)



print3 = pd.read_sql("""SELECT City_Name,Population FROM City
WHERE Population IS NULL
""",conn)

print(print3)


print4 = pd.read_sql("""SELECT City_Name,Population FROM City
WHERE Population IS NOT NULL
""",conn)

print(print4)
