# Importing SQLite
import sqlite3 as lite

# Creating connection
con = lite.connect('finan.db')

# Creating category table
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Category(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

# Creating revenues table
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Revenues(id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, added_in DATE, value DECIMAL)")

# Creating expenses table
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Expenses(id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, removed_in DATE, value DECIMAL)")

 
