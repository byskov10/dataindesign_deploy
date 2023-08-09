# %%
# Import libraries
import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

st.set_page_config(layout = "wide", page_title="Individual participant", page_icon="📊")

# –––!! Chose dataset !!–––
cwd = os.getcwd()
path_to_datasets = cwd + "/cleaned_datasets/"
files_in_folder = os.listdir(path_to_datasets)
files_in_folder.sort()

item_list = files_in_folder

# Selectbox: Chose participant
items = st.sidebar.selectbox('Chose participant dataset', item_list)
df_path = path_to_datasets + items

st.title("Participant: " + items[0:-12])


# # –––!! Import data !!–––
df_data = pd.read_csv(df_path, sep="\t")
#df_data["AOIMouse"].replace(np.nan, 'NoClick')



# –––!! Chose view !!–––
view_chosen = st.selectbox("Chose View", ["All", "Frontpage", "viz1", "viz2", "viz3", "viz4"])
if view_chosen == "Frontpage":
    view_chosen = "landingPage"

# –––!! Dataframe copy !!–––
if view_chosen == "All":
    df_data1 = df_data
else:
    df_data1 = df_data[df_data['MediaName'].str.contains(view_chosen)]

# –––!! Import image !!–––
if view_chosen == "viz1":
    viz_image = Image.open("screenshot1.png")
elif view_chosen == "viz2":
    viz_image = Image.open("screenshot2.png")
elif view_chosen == "viz3":
    viz_image = Image.open("screenshot3.png")
elif view_chosen == "viz4":
    viz_image = Image.open("screenshot4.png")
else:
    viz_image = Image.open("screenshot.png")

col1, col2 = st.columns(2)
mark_opacities = col1.slider("Mark Opacity", 0.05, 1.0, 0.3, 0.05)


# –––!! Chart !!–––
# FIG
aoi_scatter = st.checkbox('Color marks as Area of Interest')
quality_List = sorted(df_data['AOIGaze'].unique())
if aoi_scatter:
    fig = px.scatter(df_data1, x="GazeX", y="GazeY", opacity=mark_opacities, width=1920/1.5, height=1080/1.5, color="AOIGaze",
    color_discrete_map={quality_List[0]: 'red',
    quality_List[1]: 'orange',
    quality_List[2]: 'blue',
    quality_List[3]: 'white'}
    )
else:
    fig = px.scatter(df_data1, x="GazeX", y="GazeY", opacity=mark_opacities, width=1920/1.5, height=1080/1.5)

fig.add_shape(type="rect",
    x0=520, y0=210, x1=1755, y1=1120,
    layer="below",
    line=dict(
        color="RoyalBlue",
        width=2,
    ),
    fillcolor="LightSkyBlue",
)

# Add image
img_width = 1235
img_height = 910
scale_factor = 0.5
fig.update_yaxes(range=list([1440,0]))
fig.update_xaxes(range=list([0, 2560]))
fig.add_layout_image(
        x=520,
        sizex=img_width,
        y=210,
        sizey=img_height,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        source=viz_image,
        sizing="stretch"
)

# Add a second trace to the plot
clicks = st.checkbox('Clicks')
if clicks:
    fig.add_trace(go.Scatter(x=df_data1['MouseX'], y=df_data1['MouseY'], mode='markers', marker=dict(color='red')))


if view_chosen == "viz1":
    aoi = st.checkbox('Show Area of Interest?')
    if aoi:
        st.write("Orange: Controls \n Blue: Numbers")
        fig.add_shape(type="rect",
            x0=520, y0=210, x1=1755, y1=325,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=520, y0=325, x1=790, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=790, y0=1050, x1=1755, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="blue",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=1625, y0=325, x1=1755, y1=1050,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="blue",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=790, y0=325, x1=1625, y1=1050,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="red",
            opacity=0.2
        )

if view_chosen == "viz2":
    aoi = st.checkbox('Show Area of Interest?')
    if aoi:
        st.write("Orange: Controls \n Blue: Numbers")
        fig.add_shape(type="rect",
            x0=520, y0=210, x1=1755, y1=325,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=520, y0=325, x1=890, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=890, y0=1050, x1=1755, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="blue",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=1625, y0=325, x1=1755, y1=1050,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="blue",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=890, y0=325, x1=1625, y1=1050,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="red",
            opacity=0.2
        )

if view_chosen == "viz3":
    aoi = st.checkbox('Show Area of Interest?')
    if aoi:
        st.write("Orange: Controls \n Blue: Numbers")
        fig.add_shape(type="rect",
            x0=520, y0=210, x1=1755, y1=325,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=520, y0=325, x1=790, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=790, y0=325, x1=890, y1=1050,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=790, y0=1050, x1=1755, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="blue",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=890, y0=325, x1=1755, y1=1050,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="red",
            opacity=0.2
        )

if view_chosen == "viz4":
    aoi = st.checkbox('Show Area of Interest?')
    if aoi:
        st.write("Orange: Controls \n Blue: Numbers")
        fig.add_shape(type="rect",
            x0=520, y0=210, x1=1755, y1=325,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=520, y0=325, x1=790, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="orange",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=790, y0=1075, x1=1755, y1=1120,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="blue",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=1625, y0=325, x1=1755, y1=1075,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="blue",
            opacity=0.2
        )
        fig.add_shape(type="rect",
            x0=790, y0=325, x1=1625, y1=1075,
            layer="above",
            line=dict(
                width=0,
            ),
            fillcolor="red",
            opacity=0.2
        )





# Bar chart
df_click = df_data1[df_data1["MouseEvent"] == "Left"]
df_click = pd.DataFrame(df_click.groupby("ParticipantName")["View"].value_counts().reset_index(name='counts'))


fig1 = px.histogram(df_data1, title="View", x="View", text_auto=True)
fig4 = px.histogram(df_click, title="Clicks", x="View", y="counts", text_auto=True)
fig2 = px.histogram(df_data1, title="AOIGaze", x="AOIGaze", text_auto=True)
fig3 = px.histogram(df_data1, title="AOIMouse", x="AOIMouse", text_auto=True)



#st.markdown("Visualization of before and after the exact moment")
st.plotly_chart(fig)
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
col4.metric(label="GazePoints", value=len(df_data1))
col6.metric(label="Clicks", value=df_data1["MouseEvent"].value_counts().sum())
#st.markdown('<center>This text is centered</center>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig4, use_container_width=True)
col1.plotly_chart(fig2)
col2.plotly_chart(fig3)