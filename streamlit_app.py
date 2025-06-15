import streamlit as st
import pybaseball as pb

st.set_page_config(
    page_title="Baseball Analytics", 
    page_icon="⚾", 
    layout="wide",
)

# Home Page
home_page = st.Page("pages/home.py", title="Home")

# App Pages
draft_page = st.Page("pages/draft.py", title="Amateur Draft")
draft_by_team_page = st.Page("pages/draft_by_team.py", title="Amateur Draft by Team")
standings_page = st.Page("pages/standings.py", title="League Standings")

pg = st.navigation([
        home_page,
        draft_page,
        draft_by_team_page,
        standings_page
])

pg.run()
