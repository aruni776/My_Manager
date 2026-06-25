from database.task_queries import (
    get_total_tasks,
    get_completed_tasks,
    get_life_areas,
    get_top_priorities
)

from database.event_queries import (
    get_event_count
)


def load_dashboard_data():

    total_tasks = get_total_tasks()

    completed_tasks = get_completed_tasks()

    event_count = get_event_count()

    category_rows = get_life_areas()

    top_tasks = get_top_priorities()

    productivity = (
        completed_tasks / total_tasks * 100
        if total_tasks > 0
        else 0
    )

    return {

        "total_tasks": total_tasks,

        "completed_tasks": completed_tasks,

        "event_count": event_count,

        "category_rows": category_rows,

        "top_tasks": top_tasks,

        "productivity": productivity
    }