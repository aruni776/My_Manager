import streamlit as st


def render_deadlines(top_tasks):

    st.subheader(
        "Upcoming Deadlines"
    )

    if not top_tasks:

        st.info(
            "No upcoming tasks."
        )

        return

    for task in top_tasks[:5]:

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(
                    f"**{task[1]}**"
                )

                st.caption(
                    task[2]
                )

            with col2:

                st.metric(
                    "Score",
                    task[4] * task[5]
                )