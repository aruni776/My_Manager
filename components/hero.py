import streamlit as st


def render_hero():

    col1, col2 = st.columns([4, 1])

    with col1:

        st.title(
            "Welcome Back"
        )

        st.write(
            "Manage academics, events, deadlines and personal goals from a single dashboard."
        )

    with col2:

        st.metric(
            "🎯 Focus Score",
            "86"
        )

    st.divider()
