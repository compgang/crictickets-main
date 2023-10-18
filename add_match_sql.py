import sqlite3 as sql
import random as ran
import string

con = sql.connect("data.db")
cur = con.cursor()
x = int(input('''Select option: 
1. Add a match
2. Remove a match
'''))

if x == 1:
    team1 = input("Enter team 1: ")
    team2 = input("Enter team 2: ")
    cur.execute(f"select matchID from matches where Team1 = '{team1}' and Team2 = '{team2}'")
    if not cur.fetchone():
        location1 = input("Enter location: ")
        date = input("Enter date: ")
        matchID = ''.join(ran.choices(string.digits, k=6))
        cur.execute(f"select matchID from matches where matchID = '{matchID}'")
        while cur.fetchone():
            matchID = ''.join(ran.choices(string.digits, k=6))
        cur.execute("insert into matches (matchID, Team1, Team2, location, date) values (?, ?, ?, ?, ?)",
                    (matchID, team1, team2, location1, date))
        con.commit()
        print("Match has been created.")
    else:
        print("Match for these two teams already exists.")
elif x == 2:
    matchID = int(input("Enter match ID from database: "))
    cur.execute(f"delete from matches where matchID = '{matchID}'")
    con.commit()
    print("Match for", matchID, "has been deleted.")
