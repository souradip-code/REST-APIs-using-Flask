import sqlite3


connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_table)

create_table = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)'
cursor.execute(create_table)


# cursor.execute("INSERT INTO items VALUES ('chair',12.33 )")

connection.commit()
connection.close()