# Import Corner

import sqlite3 as sql
import random as ran
import string
import time
import re
import hashlib
import os
import binascii
import pwinput  #

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

# Initialize the database connection
con = sql.connect("data.db")
cur = con.cursor()

# Function to create a new account with password hashing
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

    password = pwinput.pwinput(prompt="Enter your password: ")
    password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
    while not password_valid:
        print("Password structure is invalid! Retry.")
        password = pwinput.pwinput(prompt="Enter your password: ")
        password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
        continue

    password2 = pwinput.pwinput(prompt="Enter your password again: ")

    while not password == password2:
        print("Both passwords are not the same! Retry.")
        password = pwinput.pwinput(prompt="Enter your password: ")
        password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
        while not password_valid:
            print("Password structure is invalid! Retry.")
            password = pwinput.pwinput(prompt="Enter your password: ")
            password_valid = bool(re.match(r"^(?![\s\S]*\s)\S{5,}$", password))
            continue
        password2 = pwinput.pwinput(prompt="Enter your password again: ")

    # Generate a random salt and hash the password with the salt
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    password_hash = binascii.hexlify(key + salt).decode('ascii')

    statement = f"SELECT email FROM users WHERE email = '{email}'"
    cur.execute(statement)
    if not cur.fetchone():
        userid = ''.join(ran.choices(string.ascii_uppercase + string.digits, k=10))
        cur.execute(f"SELECT userID FROM users WHERE userID = '{userid}'")
        while cur.fetchone():
            userid = ''.join(ran.choices(string.ascii_uppercase + string.digits, k=10))
        cur.execute("INSERT INTO users (userID, email, username, password_hash, salt) VALUES (?, ?, ?, ?, ?)",
                    (userid, email, username, password_hash, salt))
        con.commit()
        print("Account has been created! Please log in to your account now.")
    else:
        print("User with this email already exists! Retry.")

# Function to log into an account with password verification
def log_in():
    username = input("Enter your username: ")
    password = pwinput.pwinput(prompt="Enter your password: ")

    statement = f"SELECT email, password_hash, salt FROM users WHERE username = ?"
    cur.execute(statement, (username,))
    row = cur.fetchone()

    if not row:
        print("There exists no account with this username! Check again.")
        return False

    email, stored_password_hash, salt = row

    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    password_hash = binascii.hexlify(key + salt).decode('ascii')

    if password_hash == stored_password_hash:
        print("You have successfully logged in! Welcome", username)
        return True
    else:
        print("Incorrect username or password! Check again.")
        return False


# Function to sort matches by city and function to sort matches by date, team


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
        log_in()
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



