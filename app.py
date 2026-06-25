import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Student OS",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student OS")

st.subheader(
    "The operating system for ambitious students"
)

st.divider()

st.header("🔥 Top Priorities")

conn = sqlite3.connect(
    "student_os.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM tasks
ORDER BY
(importance * urgency) DESC
LIMIT 5
""")

tasks = cursor.fetchall()

for task in tasks:

    score = task[4] * task[5]

    st.markdown(
        f"""
### 📌 {task[1]}

Category: {task[2]}

Priority Score: {score}
"""
    )

conn.close()

# -------------------------
# PRODUCTIVITY SCORE
# -------------------------

conn = sqlite3.connect("student_os.db")
cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM tasks
""")

total_tasks = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tasks
WHERE completed = 1
""")

completed_tasks = cursor.fetchone()[0]

conn.close()

if total_tasks > 0:
    productivity = (
        completed_tasks /
        total_tasks
    ) * 100
else:
    productivity = 0

st.divider()

st.header("📊 Productivity Score")

st.metric(
    "Completion Rate",
    f"{productivity:.1f}%"
)

st.divider()

st.header("📚 Life Areas")

conn = sqlite3.connect("student_os.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    category,
    COUNT(*)
FROM tasks
GROUP BY category
""")

rows = cursor.fetchall()

conn.close()

for row in rows:

    st.metric(
        label=row[0],
        value=f"{row[1]} task(s)"
    )

conn = sqlite3.connect(
    "student_os.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM events
""")

event_count = cursor.fetchone()[0]

conn.close()

st.metric(
    "Upcoming Events",
    event_count
)


st.divider()

st.header("⚠ Schedule Alerts")