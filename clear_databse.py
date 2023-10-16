import sqlite3 as sql
import time
print("Processing....")
con = sql.connect("data.db")
cur = con.cursor()
statement = f"drop table users"
cur.execute(statement)
statement = f'''create table users 
(
email char, 
username char,
password char
)
'''
cur.execute(statement)

time.sleep(2)
print("data.db has been cleared. have a great day!")
time.sleep(2)
