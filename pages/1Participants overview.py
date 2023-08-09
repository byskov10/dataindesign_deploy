# %%
# Import libraries
import streamlit as st
import plotly.express as px
from database_actions import Database

# –––!! Page config !!–––
st.set_page_config(layout = "wide", page_title="Participants overview", page_icon="📊")
st.title("Participants overview")

# # –––!! Import data !!–––
database = Database()

df_view = database.pull_dataset("df_view")
df_view2 = database.pull_dataset("df_view2")
df_click = database.pull_dataset("df_click")
df_click2 = database.pull_dataset("df_click2")

view_colors = {
    'other': '#EF553B',
    'viz1': '#00CC96',
    'viz2': '#FFA15A',
    'viz3': '#636EFA',
    'viz4': '#AB63FA'
    }
aois_colors = {
    'Chart': '#EF553B',
    'Control': '#00CC96',
    'Other': '#FFA15A',
    'Numbers': '#636EFA',
    }

fig = px.bar(df_view, x="ParticipantName", y="counts", title="Participant GazePoints")
fig1 = px.bar(df_click, x="ParticipantName", y="counts", title="Participant Clicks")
fig2 = px.bar(df_view, x="ParticipantName", y="counts", color="View", title="Views by participant", color_discrete_map=view_colors)
fig3 = px.bar(df_view2, x="ParticipantName", y="counts", color="AOIGaze", title="AOIs by participant", color_discrete_map=aois_colors)
fig4 = px.bar(df_click, x="ParticipantName", y="counts", color="View", title="Clicks on views by participant", color_discrete_map=view_colors)
fig5 = px.bar(df_click2, x="ParticipantName", y="counts", color="AOIMouse", title="Clicks on AOIs by participant", color_discrete_map=aois_colors)

col1, col2 = st.columns(2)
col1.plotly_chart(fig, use_container_width=True)
col2.plotly_chart(fig1, use_container_width=True)
col1.plotly_chart(fig2, use_container_width=True)
col2.plotly_chart(fig4, use_container_width=True)
col1.plotly_chart(fig3, use_container_width=True)
col2.plotly_chart(fig5, use_container_width=True)