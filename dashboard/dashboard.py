from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    connection = sqlite3.connect("database/events.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM security_events")
    rows = cursor.fetchall()

    stats = {}

    cursor.execute("SELECT COUNT(*) FROM security_events")
    stats["Total Events"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM security_events WHERE event_id='4625'")
    stats["Failed Logins"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM security_events WHERE event_id='4720'")
    stats["New Users"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM security_events WHERE event_id='4728'")
    stats["Admin Group Changes"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM security_events WHERE event_id='5379'")
    stats["Credential Manager"] = cursor.fetchone()[0]

    chart_labels = list(stats.keys())
    chart_values = list(stats.values())

    connection.close()

    return render_template(
        "index.html",
        rows=rows,
        stats=stats,
        chart_labels=chart_labels,
        chart_values=chart_values
    )

if __name__ == "__main__":
    app.run(debug=True)