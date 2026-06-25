import streamlit as st


def render_focus_card(top_tasks):

    st.subheader(
        "Today's Focus"
    )

    if not top_tasks:

        st.info(
            "No tasks available."
        )

        return

    task = top_tasks[0]

    score = task[4] * task[5]

    with st.container(border=True):

        st.markdown(
            f"### {task[1]}"
        )

        st.caption(
            task[2]
        )

        st.progress(
            min(score / 100, 1.0)
        )

        st.metric(
            "Priority Score",
            score
        )