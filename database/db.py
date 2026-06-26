import sqlite3

def get_connection():

    return sqlite3.connect(
        "student_os.db",
        check_same_thread=False
    )