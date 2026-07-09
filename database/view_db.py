import sqlite3

connection = sqlite3.connect("database/events.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM security_events")

rows = cursor.fetchall()

print("\nDatabase Records:\n")

for row in rows:
    print(row)

connection.close()