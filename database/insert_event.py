import sqlite3

def insert_event(event_id, provider, computer, channel, level, time_created):

    connection = sqlite3.connect("database/events.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO security_events
    (event_id, provider, computer, channel, level, time_created)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        event_id,
        provider,
        computer,
        channel,
        level,
        time_created
    ))

    connection.commit()
    connection.close()