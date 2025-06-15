import streamlit as st

from pybaseball import amateur_draft
from datetime import date

# 1965 - Current Season 
current_year = int(date.today().year)

option_season = st.sidebar.selectbox(
    "Select a season:",
    reversed(range(1965, current_year))
)

if option_season >= 2021:
    rounds = 20
elif option_season == 2020:
    rounds = 5
elif option_season >= 2012 & option_season <= 2019:
    rounds = 40
elif option_season >= 1998 & option_season <= 2011:
    rounds = 50
else:
    rounds = 101

# Draft rounds
option_round = st.sidebar.selectbox(
    "Select a draft round:",
    range(1, rounds + 1)
)

df_draft = amateur_draft(option_season, option_round, keep_stats=False)

df_draft.rename(
    columns={
        'OvPck': 'Overall Pick',
        'Tm': 'Team',
        'Pos': 'Position',
        'Type': 'School Type',
        'Drafted Out of': 'School Name',
    },
    inplace=True
)

str_header = f"{option_season} Amateur Draft Round {option_round} Results"

st.subheader(str_header)
st.dataframe(df_draft, hide_index=True)
