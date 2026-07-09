import sqlite3

connection = sqlite3.connect("database/events.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM security_events")

rows = cursor.fetchall()

print("\nChecking for Suspicious Events...\n")

for row in rows:

    event_id = row[1]

    if event_id == "4625":
        print("[ALERT] Failed Login Detected")

    elif event_id == "4720":
        print("[ALERT] New User Account Created")

    elif event_id == "4728":
        print("[ALERT] User Added to Administrator Group")

    elif event_id == "5379":
        print("[INFO] Credential Manager Access")

    else:
        print("[NORMAL]", event_id)

connection.close()