from streamlit_calendar import calendar
from services.conflict_detector import has_conflict
from datetime import datetime, timedelta

import streamlit as st
import sqlite3
from datetime import date
from datetime import time

st.title("📅 Events")

title = st.text_input(
    "Event Title"
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

event_date = st.date_input(
    "Date"
)

start_time = st.time_input(
    "Start Time"
)

end_time = st.time_input(
    "End Time"
)

if st.button("Save Event"):

    conn = sqlite3.connect(
        "student_os.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO events(
            title,
            category,
            start_time,
            end_time
        )
        VALUES(?,?,?,?)
        """,
        (
            title,
            category,
            f"{event_date} {start_time}",
            f"{event_date} {end_time}"
        )
    )

    conn.commit()
    conn.close()

    st.success(
        "Event Saved"
    )

st.divider()

st.subheader("Saved Events")

conn = sqlite3.connect(
    "student_os.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM events
""")

events = cursor.fetchall()

conn.close()

conn = sqlite3.connect(
    "student_os.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM tasks
WHERE scheduled_date IS NOT NULL
""")

tasks = cursor.fetchall()

conn.close()

st.divider()

st.subheader("⚠ Schedule Conflicts")

conflict_found = False

for i in range(len(events)):

    for j in range(i + 1, len(events)):

        event1 = events[i]
        event2 = events[j]

        start1 = datetime.fromisoformat(
            event1[3]
        )

        end1 = datetime.fromisoformat(
            event1[4]
        )

        start2 = datetime.fromisoformat(
            event2[3]
        )

        end2 = datetime.fromisoformat(
            event2[4]
        )

        if has_conflict(
        start1,
        end1,
        start2,
        end2
        ):

            conflict_found = True

            st.warning(
            f"""
    ⚠ Schedule Conflict

    {event1[1]}
    ({event1[3]} - {event1[4]})

    overlaps with

    {event2[1]}
    ({event2[3]} - {event2[4]})
    """
            )
if not conflict_found:

    st.success(
           "No schedule conflicts found."
    )


st.divider()

st.subheader("📅 Calendar View")

category_colors = {

    "Academics": "#4285F4",
    "Sports": "#34A853",
    "Clubs": "#FBBC05",
    "Career": "#EA4335",
    "Personal": "#9C27B0",
    "Social": "#00ACC1"
}

calendar_events = []

for event in events:

    calendar_events.append(
        {
            "title": event[1],
            "start": event[3],
            "end": event[4],
            "backgroundColor":
                category_colors.get(
                    event[2],
                    "#808080"
                )
        }
    )

for task in tasks:

    calendar_events.append(
        {
            "title": f"📝 {task[1]}",
            "start": task[7],
            "end": task[7],
            "backgroundColor": "#673AB7"
        }
    )

calendar_options = {
    "initialView": "dayGridMonth"
}

calendar(
    events=calendar_events,
    options=calendar_options
)

st.divider()

st.subheader("📆 Upcoming Week")

if "selected_day" not in st.session_state:

    st.session_state["selected_day"] = date.today()

if "week_offset" not in st.session_state:

    st.session_state["week_offset"] = 0

col_prev, col_current, col_next = st.columns(3)

with col_prev:

    if st.button("⬅ Previous Week"):

        st.session_state["week_offset"] -= 7

with col_current:

    if st.button("📅 This Week"):

        st.session_state["week_offset"] = 0
        st.session_state["selected_day"] = date.today()

with col_next:

    if st.button("Next Week ➡"):

        st.session_state["week_offset"] += 7

week_days = []

week_days = []

start_day = (
    date.today()
    +
    timedelta(
        days=st.session_state["week_offset"]
    )
)

for i in range(7):

    week_days.append(
        start_day + timedelta(days=i)
    )

cols = st.columns(7)

for i, day in enumerate(week_days):

    with cols[i]:

        if st.button(
            day.strftime("%a\n%d"),
            key=f"day_{i}",
            use_container_width=True
        ):

            st.session_state["selected_day"] = day

selected_day = st.session_state["selected_day"]

st.subheader(
    f"📅 Schedule for {selected_day}"
)

st.markdown("### 📝 Tasks")

task_found = False

for task in tasks:

    if task[7] == str(selected_day):

        task_found = True

        st.info(
            f"""
{task[1]}

Category: {task[2]}

Deadline: {task[3]}
"""
        )

if not task_found:

    st.write(
        "No tasks scheduled."
    )

st.markdown("### 📅 Events")

event_found = False

for event in events:

    event_day = event[3].split()[0]

    if event_day == str(selected_day):

        event_found = True

        st.success(
            f"""
{event[1]}

Time:
{event[3].split()[1]} - {event[4].split()[1]}

Category: {event[2]}
"""
        )

if not event_found:

    st.write(
        "No events scheduled."
    )

st.divider()

st.subheader("🎨 Categories")

for category, color in category_colors.items():

    st.markdown(
        f"""
<span style="
background-color:{color};
padding:8px;
border-radius:5px;
color:white;
">
{category}
</span>
""",
        unsafe_allow_html=True
    )


st.divider()

st.subheader("📋 Manage Events")
for event in events:

    col1, col2 = st.columns([5,1])

    with col1:

        st.markdown(
            f"""
### 📅 {event[1]}

**Category:** {event[2]}

**Start:** {event[3]}

**End:** {event[4]}
"""
        )

    with col2:

        if st.button(
            "🗑 Delete",
            key=f"delete_event_{event[0]}"
        ):

            conn = sqlite3.connect(
                "student_os.db"
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM events
                WHERE id = ?
                """,
                (event[0],)
            )

            conn.commit()

            conn.close()

            st.rerun()

    st.divider()