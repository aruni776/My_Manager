from database.db import get_connection


def get_event_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM events
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result