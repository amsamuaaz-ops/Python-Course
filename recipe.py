
import sqlite3

import pandas as pd

# ---- PART 1: Build and Explore the Tables ----

conn = sqlite3.connect(':memory:')

conn.execute("CREATE TABLE recipe (recipe_id INTEGER PRIMARY KEY, recipe_name TEXT NOT NULL, cuisine TEXT NOT NULL, prep_mins INTEGER NOT NULL)")

conn.execute("CREATE TABLE ingredient (ingredient_id INTEGER PRIMARY KEY, recipe_id INTEGER NOT NULL, item TEXT NOT NULL, quantity_g INTEGER NOT NULL)")

conn.executemany("INSERT INTO recipe VALUES (?, ?, ?, ?)", [

(1, 'Pasta', 'Italian', 20),

(2, 'Tacos', 'Mexican', 15),

(3, 'Sushi', 'Japanese', 45),

(4, 'Pizza', 'Italian', 30),

(5, 'Salad', 'Greek', 10),

])

conn.executemany("INSERT INTO ingredient VALUES (?, ?, ?, ?)", [

(1, 1, 'Pasta', 200),

(2, 1, 'Sauce', 150),

(3, 2, 'Tortilla', 80),

(4, 2, 'Beef', 120),

(5, 3, 'Salmon', 180),

(6, 4, 'Dough', 250),

(7, 5, 'Lettuce', 50),

(8, 5, 'Feta', 40),

])

conn.commit()

 
allias1 = pd.read_sql("""SELECT recipe_name AS dish,cuisine AS style,prep_mins AS time FROM recipe

""",conn)

print(allias1)


allias2 = pd.read_sql("""SELECT r.recipe_name AS dish,ing.item,ing.quantity_g AS grams FROM recipe AS r
INNER JOIN ingredient AS ing ON r.recipe_id = ing.recipe_id



""",conn)

print(allias2)


allias3 = pd.read_sql("""SELECT recipe_name AS dish,cuisine AS style FROM recipe
WHERE recipe_id IN(SELECT recipe_id FROM ingredient WHERE quantity_g >100 )




""",conn)

print(allias3)


allias4 = pd.read_sql("""SELECT recipe_name AS dish,cuisine AS style,prep_mins AS time FROM recipe
WHERE prep_mins = (SELECT MIN(prep_mins) FROM recipe)
""",conn)

print(allias4)



allias5 = pd.read_sql("""SELECT recipe_name AS dish,cuisine AS style,prep_mins AS time FROM recipe
WHERE prep_mins = (SELECT MAX(prep_mins) FROM recipe)
""",conn)

print(allias5)
