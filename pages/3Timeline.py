# %%
# Import libraries
import streamlit as st
import pandas as pd
import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

st.set_page_config(layout = "wide", page_title="Timeline", page_icon="📊")


# –––!! Chose dataset !!–––
cwd = os.getcwd()
path_to_datasets = cwd + "/cleaned_datasets/"
files_in_folder = os.listdir(path_to_datasets)
files_in_folder.sort()

item_list = files_in_folder

# Selectbox: Chose participant
items = st.sidebar.selectbox('Chose participant dataset', item_list)
df_path = path_to_datasets + items

st.title("Timeline: " + items[0:-12])


# –––!! Import data !!–––
df_data = pd.read_csv(df_path, sep="\t")

# –––!! Frame slider !!–––
df_frame = st.slider('Dataset frame', 50, len(df_data), 50, 1)
index_number = df_frame

# –––!! Bar !!–––
if "02" in items:
    timeline_bar = Image.open("02_bar.png")
elif "01" in items:
    timeline_bar = Image.open("02_bar.png")
# elif "03" in items:
#     timeline_bar = Image.open("03_bar.png")
# elif "04" in items:
#     timeline_bar = Image.open("04_bar.png")
# elif "05" in items:
#     timeline_bar = Image.open("05_bar.png")
else:
    timeline_bar = Image.open("02_bar.png")
st.image(timeline_bar, caption='Blue: Landingpage, Red: Viz1, Green: Viz2, Purple: Viz3, Orange: Viz4')

# –––!! Dataframe copy !!–––
df_data1 = df_data[df_data["MediaName"] == df_data.loc[index_number, "MediaName"]]
df_data2 = df_data


# –––!! Before and after !!–––
col1, col2 = st.columns(2)
before_number = col1.slider('Before', 1, 100, 10, 1)
after_number = col2.slider('After', 1, 100, 10, 1)


before = index_number-before_number
after = index_number+after_number
df_data2 = df_data.iloc[before:after, :]

st.write(str(df_data.loc[index_number, "MediaName"]))


# –––!! Screenshot !!–––
def screen_grab(df, index_number):
    # Set the URL of the webpage you want to take a screenshot of
    link = df_data.loc[index_number, "MediaName"]

    # Create a new Chrome browser and set the window size
    driver = webdriver.Chrome()
    driver.set_window_size(1235, 910)

    # Navigate to the URL
    driver.get(link)

    # Wait for the page to load
    driver.implicitly_wait(1000000)

    # Scroll to end of header
    driver.execute_script("window.scrollBy(0, 210);")

    # Take the screenshot
    screenshot = driver.save_screenshot('background.png')

    # Close the browser
    driver.quit()


if st.button('Import screenshot'):
    screen_grab(df_data2, index_number)


# –––!! Chart !!–––
pyLogo = Image.open("background.png")

# FIG
fig = px.line(df_data2, x="GazeX", y="GazeY", width=1920/1.5, height=1080/1.5)

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
        source=pyLogo,
        sizing="stretch"
)


x_point = df_data.loc[index_number, "GazeX"]
y_point = df_data.loc[index_number, "GazeY"]

# Add a trace for the highlighted point
highlighted_trace = go.Scatter(
    x=[x_point],
    y=[y_point],
    mode='markers',
    marker=dict(
        color='blue',
        size=10,
        opacity=1
    )
)
fig.add_trace(highlighted_trace)



if "viz1" in df_data.loc[index_number, "MediaName"]:
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

if "viz2" in df_data.loc[index_number, "MediaName"]:
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

if "viz3" in df_data.loc[index_number, "MediaName"]:
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

if "viz4" in df_data.loc[index_number, "MediaName"]:
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


# FIG2
fig2 = px.scatter(df_data1, x="GazeX", y="GazeY", width=1920/1.5, height=1080/1.5, opacity=0.4)

fig2.add_shape(type="rect",
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
fig2.update_yaxes(range=list([1440,0]))
fig2.update_xaxes(range=list([0, 2560]))
fig2.add_layout_image(
        x=520,
        sizex=img_width,
        y=210,
        sizey=img_height,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        source=pyLogo,
        sizing="stretch"
)

# fig3 = px.bar(df_data, y=df_data.index, color="View")
# fig3.update_traces(marker_line_width = 0)

# fig3.update_layout(bargap=0,
#                   bargroupgap = 0,
#                  )


st.markdown("Visualization of before and after the exact moment")
st.plotly_chart(fig)
st.markdown("Visualization of all GazePoints from same url")
st.plotly_chart(fig2)
#st.plotly_chart(fig3)