import sqlite3

connection = sqlite3.connect("database/events.db")
cursor = connection.cursor()

queries = {
    "Total Events": "SELECT COUNT(*) FROM security_events",
    "Failed Logins": "SELECT COUNT(*) FROM security_events WHERE event_id='4625'",
    "New Users": "SELECT COUNT(*) FROM security_events WHERE event_id='4720'",
    "Admin Group Changes": "SELECT COUNT(*) FROM security_events WHERE event_id='4728'",
    "Credential Manager": "SELECT COUNT(*) FROM security_events WHERE event_id='5379'"
}

print("\nSecurity Statistics\n")

for title, query in queries.items():
    cursor.execute(query)
    count = cursor.fetchone()[0]
    print(f"{title}: {count}")

connection.close()