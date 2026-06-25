import streamlit as st


def render_dashboard_cards(
    total_tasks,
    event_count,
    productivity
):

    focus_score = int(productivity)

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📋 Total Tasks",
            total_tasks
        )

    with col2:

        st.metric(
            "📅 Events",
            event_count
        )

    with col3:

        st.metric(
            "⚡ Productivity",
            f"{productivity:.0f}%"
        )

    with col4:

        st.metric(
            "🎯 Focus",
            focus_score
        )