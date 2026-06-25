import streamlit as st


def render_sidebar(themes):

    st.sidebar.title(
        "Student OS"
    )

    st.sidebar.caption(
        "Academic Command Center"
    )

    st.sidebar.divider()

    selected_theme = st.sidebar.selectbox(
        "Theme",
        list(themes.keys())
    )

    return selected_theme