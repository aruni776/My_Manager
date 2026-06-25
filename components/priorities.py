import streamlit as st


def render_priorities(top_tasks):

    st.subheader(
        "Top Priorities"
    )

    if not top_tasks:

        st.info(
            "No tasks available."
        )

        return

    for task in top_tasks:

        score = task[4] * task[5]

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(
                    f"### {task[1]}"
                )

                st.caption(
                    f"📂 {task[2]}"
                )

                st.progress(
                    min(score / 100, 1.0)
                )

            with col2:

                st.metric(
                    "Priority",
                    score
                )