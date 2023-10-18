import sqlite3 as sql
import time
print("Processing....")
con = sql.connect("data.db")
cur = con.cursor()
statement = f"drop table users"

cur.execute(statement)
statement = f'''create table users 
(
userID char primary key,
email char, 
username char,
password char
)
'''
cur.execute(statement)
statement = f"drop table orders"
cur.execute(statement)

statement = (f'''create table orders
(
userID char primary key, 
email char,
matchID int,
seatnum char,
foodndrinks bool,
transport bool
)
''')
cur.execute(statement)

time.sleep(2)
print("data.db has been cleared. have a great day!")
time.sleep(2)
