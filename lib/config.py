# import sqlite3
import sqlite3
from student import Student

#create a database connection
conn = sqlite3.connect("db/moringa.db")

# execute a query to create a table in moringa.db
# get access to the cursor object

c = conn.cursor()
# # print(help(c))
# c.execute(
#     '''CREATE TABLE students(
#     id INTEGER PRIMARY KEY,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     age INTEGER,
#     gender TEXT,
#     phone INTEGER,
#     username TEXT NOT NULL
#     email TEXT NOT NULL
#     )'''
# )

# c.execute()


