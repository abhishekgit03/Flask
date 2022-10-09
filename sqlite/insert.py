import sqlite3
conn = sqlite3.connect('database.db')
print("Connected Successfully")
conn.execute("INSERT INTO students(name,age,city) Values('Abhishek',19,'Durgapur')")
conn.commit()
print("Added data")
conn.close()