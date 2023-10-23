import sqlite3 as sql
import time
print("Processing....")
con = sql.connect("data.db")
cur = con.cursor()
cur.execute(f"drop table users")


cur.execute(f'''create table users 
(
userID char primary key,
email char, 
username char,
password char
)
''')

cur.execute(f"drop table orders")


cur.execute(f'''create table orders
(
userID char primary key, 
email char,
matchID int,
seat_num char,
food_n_drinks bool,
transport bool
)
''')



time.sleep(2)
print("data.db has been cleared. have a great day!")
time.sleep(2)
