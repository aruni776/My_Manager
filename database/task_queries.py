from database.db import get_connection


def get_total_tasks():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM tasks
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result


def get_completed_tasks():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM tasks
    WHERE completed = 1
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result


def get_life_areas():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        category,
        COUNT(*)
    FROM tasks
    GROUP BY category
    """)

    result = cursor.fetchall()

    conn.close()

    return result


def get_top_priorities():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM tasks
    ORDER BY
    (importance * urgency) DESC
    LIMIT 5
    """)

    result = cursor.fetchall()

    conn.close()

    return result