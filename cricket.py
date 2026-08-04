
import sqlite3

import pandas as pd

conn = sqlite3.connect('MYSQL/cricket.db')

cursor = conn.cursor()

cursor.executescript("""

DROP TABLE IF EXISTS Team;

DROP TABLE IF EXISTS Match;

DROP TABLE IF EXISTS Player_Match;

CREATE TABLE Team (

Team_Id INTEGER PRIMARY KEY,

Team_Name TEXT

);

CREATE TABLE Match (

Match_Id INTEGER PRIMARY KEY,

Season_Id INTEGER,

Match_Winner INTEGER,

Win_Margin INTEGER

);

CREATE TABLE Player_Match (

Match_Id INTEGER,

Player_Id INTEGER

);

INSERT INTO Team VALUES

(1,'Chennai Super Kings'),(2,'Delhi Capitals'),

(3,'Deccan Chargers'),(4,'Delhi Daredevils'),

(5,'Mumbai Indians'),(6,'Kolkata Knight Riders'),

(7,'Rajasthan Royals'),(8,'Kings XI Punjab');

INSERT INTO Match VALUES

(1,7,5,35),(2,7,5,22),(3,8,5,45),(4,8,5,8),

(5,8,1,67),(6,8,6,19),(7,9,5,33),(8,9,1,28),

(9,9,5,12),(10,9,6,55),(11,9,3,38),(12,9,7,4);

INSERT INTO Player_Match VALUES

(1,101),(1,102),(2,103),(3,101),(4,104),(5,102);

""")

conn.commit()

print('Database ready!')


matches = pd.read_sql("""SELECT *

FROM Match;""", conn)

print(matches)

print('Rows and columns:', matches.shape)

alldata = pd.read_sql("""SELECT Team_id,Team_Name FROM Team 

""",conn)

print(alldata)

print('Rows and columns:', alldata.shape)

matchwinner = pd.read_sql("""SELECT Season_Id,Match_id,Match_Winner FROM Match
WHERE Match_Winner >=5 AND Season_Id IN(8,9)
""",conn)

print(matchwinner)


print('Rows and columns:', matchwinner.shape)

teamnam1 = pd.read_sql("""SELECT Team_Name FROM Team
WHERE Team_Name LIKE "De%"                           
""",conn)

print(teamnam1)


print('Rows and columns:', teamnam1.shape)


teamnam2 = pd.read_sql("""SELECT Team_Name FROM Team
WHERE Team_Name LIKE "%Kings"                           
""",conn)

print(teamnam2)


print('Rows and columns:', teamnam2.shape)

totalmatch = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin) FROM Match
                   
""",conn)

print(totalmatch)
print('Rows and columns:', totalmatch.shape)

totalseasonid = totalmatch = pd.read_sql("""SELECT MIN(Season_Id), MAX(Season_Id) FROM Match
                   
""",conn)
print(totalseasonid)
print('Rows and columns:', totalseasonid.shape)

conn.close()




