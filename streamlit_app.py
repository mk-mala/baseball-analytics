import streamlit as st
import pybaseball as pb

st.set_page_config(page_title="Baseball Analytics", page_icon="⚾")

home_page = st.Page("pages/home.py", title="Home")

standings_page = st.Page("pages/standings.py", title="League Standings")

pg = st.navigation([home_page, standings_page])

pg.run()
