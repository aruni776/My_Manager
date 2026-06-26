import sqlite3

conn = sqlite3.connect("student_os.db")
cursor = conn.cursor()

try:

    cursor.execute("""
    ALTER TABLE tasks
    ADD COLUMN scheduled_date TEXT
    """)

    print("Column Added")

except:

    print("Column Already Exists")

conn.commit()
conn.close()