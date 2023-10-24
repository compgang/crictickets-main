import sqlite3
import string
import random as ran

# Connect to the database
conn = sqlite3.connect('data.db')

# Create a cursor object
cur = conn.cursor()



userid1 = ''.join(ran.choices(string.ascii_uppercase, k=4))
userid2 = ''.join(ran.choices(string.digits, k=10))
userid3 = str(userid1) + str(userid2)
print (userid3)
cur.execute(f"select orderid from matches where orderID = '{userid3}'")

