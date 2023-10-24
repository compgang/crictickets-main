# Import Corner

import sqlite3 as sql
import time
import pwinput as mask
import re
import random as ran
import string

# Initialize the database connection
con = sql.connect("data.db")
cur = con.cursor()

# Function Definition Corner

# Function for Login system


def login_screen_choice():
    time.sleep(1)
    print("Welcome to CricTickets, the best place to get your IPL tickets!")
    time.sleep(3)

    x = int(input('''1. Create a new account
2. Log into your account
3. Continue browsing without an account
What is your choice?: '''))
    return x


# Function to create a new account


def create_account():
    print("Here are some rules to follow while creating your new account: ")
    time.sleep(3)
    print('''1. Your username must be at least 5 characters and must only include lowercase letters, numbers, 
and underscores. No other character is accepted. ''')
    time.sleep(5)
    print('''2. Your password must be at least 5 characters and must not include any whitespaces. Also, please
refrain from using simple passwords.''')
    time.sleep(5)

    email = input("Enter your E-mail: ")
    email_valid = bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
    while not email_valid:
        print("Email entered is invalid! Retry.")
        email = input("Enter your E-mail: ")
        email_valid = bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
        continue

    username = input("Enter your username: ")
    username_valid = bool(re.match(r"^[a-z0-9_]{5,}$", username))
    while not username_valid:
        print("Username is invalid! Retry.")
        username = input("Enter your username: ")
        username_valid = bool(re.match(r"^[a-z0-9_]{5,}$", username))
        continue

    password = mask.pwinput(prompt="Enter your password: ", mask='*')
    password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
    while not password_valid:
        print("Password structure is invalid! Retry.")
        password = mask.pwinput(prompt="Enter your password: ", mask='*')
        password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
        continue

    password2 = mask.pwinput(prompt="Enter your password again: ", mask='*')

    while not password == password2:
        print("Both passwords are not the same! Retry.")
        password = mask.pwinput(prompt="Enter your password: ", mask='*')
        password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
        while not password_valid:
            print("Password structure is invalid! Retry.")
            password = mask.pwinput(prompt="Enter your password: ", mask='*')
            password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
            continue
        password2 = mask.pwinput(prompt="Enter your password again: ", mask='*')

    statement = f"SELECT email FROM users WHERE email = '{email}'"
    cur.execute(statement)
    if not cur.fetchone():
        userid = ''.join(ran.choices(string.ascii_uppercase + string.digits, k=10))
        cur.execute(f"select userID from users where userID = '{userid}'")
        while cur.fetchone():
            userid = ''.join(ran.choices(string.ascii_uppercase + string.digits, k=10))
        cur.execute("insert into users (userID, email, username, password) values (?, ?, ?, ?)",
                    (userid, email, username, password))
        con.commit()
        print("Account has been created! Please log in to your account now.")
        return
    else:
        print("User with this email already exists! Retry.")


# Function to log into an account

def log_in():
    username = input("Enter your username: ")
    password = mask.pwinput(prompt="Enter your password: ", mask='*')

    statement = f"SELECT email from users where username = '{username}'"
    cur.execute(statement)
    if not cur.fetchone():
        print("There exists no account with this username! Check again.")
        return False

    else:

        statement = f"SELECT username from users WHERE username = ? AND password = ?"
        cur.execute(statement, (username, password))
        if not cur.fetchone():
            print("Incorrect username or password! Check again.")
            return False
        else:
            print("You have successfully logged in! Welcome", username)
            return True


# Function to sort matches by city


# function to sort matches by date, team, stadium


# function for match description
def print_description():

    # Use parameterized queries to avoid SQL injection
    cur.execute("SELECT * FROM matches WHERE (Team1 = ? AND Team2 = ?) OR (Team1 = ? AND Team2 = ?)",
                (team1, team2, team2, team1)) # Need to be changed based on Khushi's variable names

    match_data = cur.fetchone()  # Use fetchone to retrieve a single match
    i = 1
    for row in match_data:
        match_id, team1, team2, location, date, stadium, desc, price_range, time1 = match_data
        print(i,":")
        print(f"Match: {team1} vs {team2}")
        print(f"Location: {location}")
        print(f"Stadium: {stadium}")
        print(f"Time: {time1}")
        print(f'''Description: \n
{desc}''')
        print(f"Price range: {price_range}")
        print("Book now!!")
        i += 1
    else:
        print("No matching records found for the given teams.")


# function for seat selection


# function for accessories


# function for payment


# function to print invoice


# function for logout


# don't forget to give a go back option after each step


# Main program


if __name__ == "__main__":

    answer = login_screen_choice()

    if answer == 1:
        create_account()
    elif answer == 2:
        if log_in():
            # Perform actions after successful login here
            pass
        else:
            log_in()
    elif answer == 3:
        # Continue browsing without an account
        pass

    time.sleep(2)
