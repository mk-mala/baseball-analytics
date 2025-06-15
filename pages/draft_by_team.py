import streamlit as st

from pybaseball import amateur_draft_by_team
from src.data import team_code
from datetime import date

# Get Team Codes
df_team_code = team_code.df_team_code

# 1969 - Current Season 
current_year = int(date.today().year)

season = st.sidebar.selectbox(
    "Select a season:",
    reversed(range(1969, current_year))
)

team = st.sidebar.selectbox(
    "Select a team:",
    df_team_code['team_name']
)

team_code = df_team_code[df_team_code['team_name'] == team]['team_code']

df_draft_by_team_year = amateur_draft_by_team(team_code, season, keep_stats=False)

df_draft_by_team_year.rename(
    columns={'OvPck': 'Overall Pick',
             'Tm': 'Team',
             'Pos': 'Position',
             'Type': 'School Type',
             'Drafted Out of': 'School Name',
    },
    inplace=True
)

str_header = f"{season} {team} Amateur Draft Results"

st.subheader(str_header)
st.dataframe(df_draft_by_team_year, hide_index=True)
