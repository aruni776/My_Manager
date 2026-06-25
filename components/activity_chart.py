import streamlit as st
import plotly.express as px


def render_activity_chart(category_rows):

    st.subheader(
        "Activity Distribution"
    )

    if not category_rows:
        return

    labels = []
    values = []

    for category, count in category_rows:

        labels.append(category)
        values.append(count)

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.55
    )

    fig.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )