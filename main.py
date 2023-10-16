# Made with love by Arnav, Khushi, Shreya and Ashvath (we need the marks)
# CricTickets™ is a trademarked name by Arnav & Co. (jk)

# Import corner
import sqlite3 as sql   # Dependency 1
import time
import pwinput as mask
import re


time.sleep(1)
print("Welcome to CricTickets, the best place to get your IPL tickets!")
time.sleep(3)

# Starting with the log in system

x = 0
a = 0
con = sql.connect("data.db")
cur = con.cursor()
while x != 1 and x != 2:
    a = 0
    x = int(input('''1. Create a new account
2. Log into your account
What is  your choice?: '''))
    while a == 0:
        if x == 2:
            username = input("Enter your username: ")
            password = mask.pwinput(prompt="Enter your password: ", mask='*')

            statement = f"SELECT username from users WHERE username = ? AND password = ?"
            cur.execute(statement, (username, password))
            if not cur.fetchone():  # An empty result evaluates to False.
                print("Incorrect username or password! Check again.")
                continue
            else:
                print("You have successfully logged in! Welcome", username, "!")
                a = 1
                x = 1
        elif x == 1:
            email = input("Enter your E-mail: ")
            email_valid = bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

            if email_valid:
                username = input("Enter your username: ")
                password = mask.pwinput(prompt="Enter your password: ", mask='*')
                password2 = mask.pwinput(prompt="Enter your password again: ", mask='*')
                while password != password2:
                    print("Both passwords do not match! Try again.")
                    username = input("Enter your username: ")
                    password = mask.pwinput(prompt="Enter your password: ", mask='*')
                    password2 = mask.pwinput(prompt="Enter your password again: ", mask='*')

                statement = f"SELECT email FROM users WHERE email = ? and username = ?"
                cur.execute(statement, (email, username))
                if not cur.fetchone():
                    cur.execute("insert into users (email, username, password) values (?, ?, ?)",
                            (email, username, password))
                    con.commit()
                    print("Account has been created! Please log in to your account now.")
                    x = 0
                    a = 1
                else:
                    print("A user is already registered to this E-mail! Retry.")
            else:
                print("This is an invalid email! Retry.")
time.sleep(10)

# Log in system finished
