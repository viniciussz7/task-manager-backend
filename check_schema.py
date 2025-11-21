import sqlite3

conn = sqlite3.connect("app.db")
c = conn.cursor()

print("Schema tasks:\n")
for row in c.execute("PRAGMA table_info(tasks);"):
    print(row)

conn.close()
