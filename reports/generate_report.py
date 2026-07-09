import sqlite3

connection = sqlite3.connect("database/events.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM security_events")
rows = cursor.fetchall()

with open("reports/security_report.txt", "w") as report:
    report.write("Windows Security Event Report\n")
    report.write("=" * 60 + "\n\n")

    for row in rows:
        report.write(f"ID: {row[1]}\n")
        report.write(f"Provider: {row[2]}\n")
        report.write(f"Computer: {row[3]}\n")
        report.write(f"Channel: {row[4]}\n")
        report.write(f"Level: {row[5]}\n")
        report.write(f"Time: {row[6]}\n")
        report.write("-" * 60 + "\n")

connection.close()

print("Report Generated Successfully!")