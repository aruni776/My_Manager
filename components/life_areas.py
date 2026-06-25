import streamlit as st


def render_life_areas(category_rows):

    st.subheader(
        "Life Areas"
    )

    if not category_rows:

        st.info(
            "No task data available."
        )

        return

    total = sum(
        count
        for _, count in category_rows
    )

    for category, count in category_rows:

        percentage = (
            count / total
            if total > 0
            else 0
        )

        with st.container(border=True):

            st.markdown(
                f"### {category}"
            )

            st.progress(
                percentage
            )

            st.caption(
                f"{count} tasks • {percentage:.0%}"
            )