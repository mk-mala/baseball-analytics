import streamlit as st
import pybaseball as pb

from datetime import date

current_year = int(date.today().year)

st.title("League Standings")

season = st.sidebar.selectbox(
    "Select a season:",
    reversed(range(1969, current_year + 1))
)

df_standings = pb.standings(season)

if season >= 1969 and season < 1994:
    
    df_standings_al_east = df_standings[0]
    df_standings_al_west = df_standings[1]

    df_standings_nl_east = df_standings[2]
    df_standings_nl_west = df_standings[3]

if season >= 1994:

    df_standings_al_east = df_standings[0]
    df_standings_al_central = df_standings[1]
    df_standings_al_west = df_standings[2]

    df_standings_nl_east = df_standings[3]
    df_standings_nl_central = df_standings[4]
    df_standings_nl_west = df_standings[5]

st.subheader("American League East")
st.dataframe(df_standings_al_east)

if season >= 1994:

    st.subheader("American League Central")
    st.dataframe(df_standings_al_central)

st.subheader("American League West")
st.dataframe(df_standings_al_west)

st.subheader("National League East")
st.dataframe(df_standings_nl_east)

if season >= 1994:

    st.subheader("National League Central")
    st.dataframe(df_standings_nl_central)

st.subheader("National League West")
st.dataframe(df_standings_nl_west)