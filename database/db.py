import sqlite3

connection = sqlite3.connect("database/events.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS security_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT,
    provider TEXT,
    computer TEXT,
    channel TEXT,
    level TEXT,
    time_created TEXT
)
""")

connection.commit()
connection.close()

print("Database Created Successfully")