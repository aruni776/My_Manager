import streamlit as st


def render_productivity(
    productivity,
    completed_tasks
):

    st.subheader(
        "Productivity Overview"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Completion Rate",
            f"{productivity:.1f}%"
        )

    with col2:

        st.metric(
            "Completed Tasks",
            completed_tasks
        )