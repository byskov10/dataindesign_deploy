# %%
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
#import sql_pull_dataset
from database_actions import Database

st.set_page_config(layout = "wide", page_title="Participants overview", page_icon="📊")

# –––!! Chose dataset !!–––


st.title("Participants overview")


# # –––!! Import data !!–––
# cwd = os.getcwd()
# path_to_datasets = cwd + "/cleaned_datasets/participants_info.csv"
# df_data = pd.read_csv(path_to_datasets)
database = Database()
df_data = database.pull_dataset("participants_info")
df_data.rename(columns={"unnamed": "Unnamed", "participantname": "ParticipantName", "gazepoints": "GazePoints", "clicks":"Clicks"}, inplace=True)

fig = px.bar(df_data, x="ParticipantName", y="GazePoints", title="Participant GazePoints")
fig1 = px.bar(df_data, x="ParticipantName", y="Clicks", title="Participant Clicks")

col1, col2 = st.columns(2)
col1.plotly_chart(fig, use_container_width=True)
col2.plotly_chart(fig1, use_container_width=True)
