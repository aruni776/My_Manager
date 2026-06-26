import streamlit as st

from assets.themes import THEMES
from assets.theme import apply_theme

from components.sidebar import render_sidebar
from components.hero import render_hero
from components.dashboard import render_dashboard_cards
from components.priorities import render_priorities
from components.life_areas import render_life_areas
from components.productivity import render_productivity
from components.alerts import render_alerts
from components.focus import render_focus_card

from database.init_db import initialize_database


from database.dashboard_queries import (
    load_dashboard_data
)
from components.activity_chart import (
    render_activity_chart
)
from components.deadlines import (
    render_deadlines
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Student OS",
    page_icon="🎓",
    layout="wide"
)

initialize_database()
# =====================================================
# SIDEBAR
# =====================================================

selected_theme = render_sidebar(
    THEMES
)

theme = THEMES[selected_theme]

# =====================================================
# THEME
# =====================================================

st.markdown(
    apply_theme(theme),
    unsafe_allow_html=True
)

# =====================================================
# DATA
# =====================================================

data = load_dashboard_data()

# =====================================================
# HERO
# =====================================================

render_hero()

# =====================================================
# DASHBOARD CARDS
# =====================================================

render_dashboard_cards(
    data["total_tasks"],
    data["event_count"],
    data["productivity"]
)

st.divider()

render_focus_card(
    data["top_tasks"]
)

st.divider()

# =====================================================
# MAIN GRID
# =====================================================

left_col, right_col = st.columns([2, 1])

with left_col:

    render_priorities(
        data["top_tasks"]
    )

with right_col:

    render_life_areas(
        data["category_rows"]
    )

# =====================================================
# PRODUCTIVITY
# =====================================================

render_productivity(
    data["productivity"],
    data["completed_tasks"]
)

st.divider()

chart_col, deadline_col = st.columns([2, 1])

with chart_col:

    render_activity_chart(
        data["category_rows"]
    )

with deadline_col:

    render_deadlines(
        data["top_tasks"]
    )

# =====================================================
# ALERTS
# =====================================================

render_alerts()