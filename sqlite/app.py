import sqlite3
conn=sqlite3.connect('database.db')
print("Connected successfully")
conn.execute('CREATE TABLE students(name TEXT, age TEXT, city TEXT )')
print("Table created successfully")

conn.close()