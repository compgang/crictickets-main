import sqlite3 as sql
con = sql.connect("data.db")
cur = con.cursor()

statement = (f'''''')

cur.execute(statement)

# Copy above execution to clear_database for presentation.