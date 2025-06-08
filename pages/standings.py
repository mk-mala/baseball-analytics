import streamlit as st
import pybaseball as pb

from datetime import date

st.title("League Standings")

# 1969 - Current Season Standings
current_year = int(date.today().year)

season = st.sidebar.selectbox(
    "Select a season:",
    reversed(range(1969, current_year + 1))
)

df_standings = pb.standings(season)

# Rename column headers
for key, value in enumerate(df_standings):
    df_standings[key]["Team"] = df_standings[key].pop("Tm")
    df_standings[key]["Wins"] = df_standings[key].pop("W")
    df_standings[key]["Losses"] = df_standings[key].pop("L")
    df_standings[key]["Win-Loss %"] = df_standings[key].pop("W-L%")
    df_standings[key]["Games Back"] = df_standings[key].pop("GB")

# Division Play Era
if season >= 1969 and season < 1994:
    
    df_standings_al_east = df_standings[0]
    df_standings_al_west = df_standings[1]

    df_standings_nl_east = df_standings[2]
    df_standings_nl_west = df_standings[3]

# Wild Card Era
if season >= 1994:

    df_standings_al_east = df_standings[0]
    df_standings_al_central = df_standings[1]
    df_standings_al_west = df_standings[2]

    df_standings_nl_east = df_standings[3]
    df_standings_nl_central = df_standings[4]
    df_standings_nl_west = df_standings[5]

# League Standings
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
