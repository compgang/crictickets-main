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
seat_num char,
food_n_drinks bool,
transport bool
)
''')
cur.execute(statement)
cur.execute("drop table matches")
cur.execute(f'''create table matches
(
matchID int,
Team1 char,
Team2 char, 
location char, 
date date,
stadium char,
desc char, 
price_range char, 
time1 time
)
''')

time.sleep(2)
print("data.db has been cleared. have a great day!")
time.sleep(2)
