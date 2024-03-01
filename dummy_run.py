import mysql.connector as mysql
con = mysql.connect(
host  = "localhost",
username = "root",
password = "mysql",
)
cur = con.cursor()

cur.execute("drop database ('cricktickets-db-exported',)")