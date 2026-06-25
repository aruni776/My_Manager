import streamlit as st
import sqlite3

st.title("📝 Tasks")

task_name = st.text_input(
    "Task Name"
)

category = st.selectbox(
    "Category",
    [
        "Academics",
        "Sports",
        "Clubs",
        "Career",
        "Personal",
        "Social"
    ]
)

importance = st.slider(
    "Importance",
    1,
    10
)

urgency = st.slider(
    "Urgency",
    1,
    10
)

deadline = st.date_input(
    "Deadline"
)
scheduled_date = st.date_input(
    "Schedule For",
    max_value=deadline
)


if st.button("Save Task"):

    conn = sqlite3.connect(
        "student_os.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks(
            title,
            category,
            deadline,
            importance,
            urgency,
            completed,
            scheduled_date
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            task_name,
            category,
            str(deadline),
            importance,
            urgency,
            0,
            str(scheduled_date)
        )
    )

    conn.commit()

    conn.close()

    st.success("Task Saved Successfully")


    st.divider()

st.subheader("Saved Tasks")

conn = sqlite3.connect(
    "student_os.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM tasks
ORDER BY completed ASC,
(importance * urgency) DESC
""")

tasks = cursor.fetchall()

conn.close()

for task in tasks:

    task_id = task[0]

    score = task[4] * task[5]

    col1, col2, col3 = st.columns([5,1,1])

    with col1:

        st.markdown(
            f"""
### 📌 {task[1]}

Category: {task[2]}

Priority Score: {score}
"""
        )

    with col2:

        if task[6] == 0:

            if st.button(
                "✅ Complete",
                key=f"complete_{task_id}"
            ):

                conn = sqlite3.connect(
                    "student_os.db"
                )

                cursor = conn.cursor()

                cursor.execute(
                    """
                    UPDATE tasks
                    SET completed = 1
                    WHERE id = ?
                    """,
                    (task_id,)
                )

                conn.commit()

                conn.close()

                st.rerun()

        else:

            st.success("Done")


    with col3:

        if st.button(
            "🗑 Delete",
            key=f"delete_{task_id}"
        ):

            conn = sqlite3.connect(
                "student_os.db"
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM tasks
                WHERE id = ?
                """,
                (task_id,)
            )

            conn.commit()

            conn.close()

            st.rerun()

            conn = sqlite3.connect(
                    "student_os.db"
                )

            cursor = conn.cursor()

            cursor.execute(
                    """
                    DELETE FROM tasks
                    WHERE id = ?
                    """,
                    (task_id,)
                )

            conn.commit()

            conn.close()

            st.rerun()