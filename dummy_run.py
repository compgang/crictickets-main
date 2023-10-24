import sqlite3
import string
import random as ran

# Connect to the database
conn = sqlite3.connect('data.db')

# Create a cursor object
cur = conn.cursor()


matchID = ''.join(ran.choices(string.digits, k=6))
cur.execute(f"select matchID from matches where matchID = '{matchID}'")
while cur.fetchone():
    matchID = ''.join(ran.choices(string.digits, k=6))

print(matchID)

a = ran.randint(650, 1000)
a_char = str(a)
while a_char[2] != '0':
    a = ran.randint(650, 1000)
    a_char = str(a)

b = ran.randint(10000, 15000)
b_char = str(b)
while b_char[-2] != '0' or b_char[-1] != '0':
    b = ran.randint(10000, 15000)
    b_char = str(b)

print(a, "-", b)
