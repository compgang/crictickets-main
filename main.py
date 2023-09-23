# Made with love by Arnav, Khushi, Shreya and Ashvath (we need the marks)
# CricTickets™ is a trademarked name by Arnav & Co. (jk)
import sqlite3 as sql
import time


time.sleep(1)
print("Welcome to CricTickets, the best place to get your IPL tickets!")
time.sleep(3)

# Starting with the log in system
x = 0
a = 0
con = sql.connect("data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (email, username, password)")
while x == 0 or x != 1 or x != 2:
    a = 0
    x = int(input('''1. Create a new account
2. Log into your account
What is  your choice?: '''))
    while a == 0:
        if x == 2:
            username = input("Enter your username!: ")
            password = input("Enter your password!: ")

            statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
            cur.execute(statement)
            if not cur.fetchone():  # An empty result evaluates to False.
                print("Incorrect username or password! Check again.")
                continue
            else:
                print("You have successfully logged in! Welcome", username, "!")
                a = 1
                x = 0
                break
        elif x == 1:
            email = input("Enter your E-mail: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            password2 = input("Enter your password again: ")
            while password != password2:
                print("Both the passwords entered do not match! Try again.")
                email = input("Enter your E-mail: ")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                password2 = input("Enter your password again: ")
            cur.execute("insert into users (email, username, password) values (?, ?, ?)",
                        (email, username, password))
            x = 0
            a = 1
            continue

# Log in system finish

