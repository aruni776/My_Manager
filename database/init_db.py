import sqlite3


def initialize_database():

    conn = sqlite3.connect("student_os.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        deadline TEXT,
        importance INTEGER,
        urgency INTEGER,
        completed INTEGER,
        scheduled_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        start_time TEXT,
        end_time TEXT
    )
    """)

    conn.commit()
    conn.close()