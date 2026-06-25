import sqlite3

def connect():

    conn = sqlite3.connect(
        "student_os.db",
        check_same_thread=False
    )

    return conn