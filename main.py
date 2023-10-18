# Made with love by Arnav, Khushi, Shreya and Ashvath (we need the marks)
# CricTickets™ is a trademarked name by Arnav & Co. (jk)

# Import corner
import sqlite3 as sql   # Dependency 1
import time
import pwinput as mask
import re
import random as ran
import string

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
            print("Here are some rules to follow while creating your new account: ")
            time.sleep(3)
            print('''1. Your username must be at least 5 characters, and must only include lowercase letters, numbers 
and underscores. No other character is accepted. ''')
            time.sleep(5)
            print('''2. Your password must be at least 5 characters, and must not include any whitespaces. Also, please
refrain from using simple passwords.''')
            time.sleep(5)
            print("3. If you make a mistake in any of the above, you will be forced to retry from the email section.")
            time.sleep(3)
            create_loop = 0
            while create_loop == 0:
                email = input("Enter your E-mail: ")
                email_valid = bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
                username = input("Enter your username: ")
                username_valid = bool(re.match(r"^[a-z0-9_]{5,}$", username))
                password = mask.pwinput(prompt="Enter your password: ", mask='*')
                password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
                password2 = mask.pwinput(prompt="Enter your password again: ", mask='*')
                if not email_valid:
                    print("Email entered is invalid! Retry.")
                elif not username_valid:
                    print("Username is invalid! Retry.")
                elif not password_valid:
                    print("Password structure is invalid! Retry.")
                elif not password == password2:
                    print("Both passwords are not same! Retry.")
                else:
                    statement = f"SELECT email FROM users WHERE email ='{email}'"
                    cur.execute(statement)
                    if not cur.fetchone():
                        userID = ''.join(ran.choices(string.ascii_uppercase + string.digits, k=10))
                        cur.execute(f"select userID from users where userID = '{userID}'")
                        while cur.fetchone():
                            userID = ''.join(ran.choices(string.ascii_uppercase + string.digits, k=10))
                            userID = str(userID)
                            cur.execute(f"select userID from users where userID = '{userID}'")
                        cur.execute("insert into users (userID, email, username, password) values (?, ?, ?, ?)",
                                    (userID, email, username, password))
                        con.commit()
                        print("Account has been created! Please log in to your account now.")
                        x = 0
                        a = 1
                        create_loop = 1
                    else:
                        print("User with this email already exists! Retry.")
time.sleep(10)

# Log in system finished
