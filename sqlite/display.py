import sqlite3
conn=sqlite3.connect("database.db")
print("Connected successfully")
cur=conn.execute("SELECT name, age, city from students")
for data in cur:
    print(data)
conn.close()