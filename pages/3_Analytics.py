import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("📊 Analytics")

conn = sqlite3.connect(
    "student_os.db"
)

query = """
SELECT
    category,
    COUNT(*) as total
FROM tasks
GROUP BY category
"""

df = pd.read_sql_query(
    query,
    conn
)

conn.close()

st.subheader(
    "📚 Task Distribution"
)

fig = px.pie(
    df,
    names="category",
    values="total"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader(
    "🏆 Most Active Area"
)

if not df.empty:

    top_category = df.loc[
        df["total"].idxmax()
    ]

    st.success(
        f"""
Most Active Area:
{top_category['category']}

Tasks:
{top_category['total']}
"""
    )

st.divider()

total_tasks = df["total"].sum()

st.metric(
    "Total Tasks",
    total_tasks
)

conn = sqlite3.connect(
    "student_os.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM tasks
""")

total = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tasks
WHERE completed = 1
""")

completed = cursor.fetchone()[0]

conn.close()

if total > 0:

    productivity = (
        completed /
        total
    ) * 100

else:

    productivity = 0

st.metric(
    "Productivity",
    f"{productivity:.1f}%"
)