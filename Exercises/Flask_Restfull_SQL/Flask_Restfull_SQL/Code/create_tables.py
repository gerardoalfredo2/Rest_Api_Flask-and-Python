import sqlite3
"""initial creation of tables"""

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS tblUser(UserId INTEGER PRIMARY KEY ,UserName text , password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items(name text ,price real)"
cursor.execute(create_table)


connection.commit()

connection.close()
