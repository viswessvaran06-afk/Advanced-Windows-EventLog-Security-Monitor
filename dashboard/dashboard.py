from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    connection = sqlite3.connect("database/events.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM security_events")
    rows = cursor.fetchall()

    connection.close()

    html = """
    <html>
    <head>
        <title>Security Dashboard</title>
    </head>

    <body>

    <h1>Windows Security Dashboard</h1>

    <table border="1" cellpadding="8">

    <tr>
        <th>ID</th>
        <th>Event ID</th>
        <th>Provider</th>
        <th>Computer</th>
        <th>Channel</th>
        <th>Level</th>
        <th>Time</th>
    </tr>

    {% for row in rows %}

    <tr>
        {% for col in row %}
        <td>{{ col }}</td>
        {% endfor %}
    </tr>

    {% endfor %}

    </table>

    </body>
    </html>
    """

    return render_template_string(html, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)