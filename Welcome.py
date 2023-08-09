# %%
#pipreqs --encoding=utf8 --force
# Import libraries
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Welcome!", page_icon="📊")

st.title("Welcome!")
st.caption("""This data visualization tool presents the data collected from a study by Blascheck et al. and the study is described by them in the paper “Exploration Strategies for Discovery of Interactivity in Visualizations”. (2018)

The following dataframe is an example of a cleaned dataset from one of the participants in the study.""")

# # –––!! Import data !!–––
cwd = os.getcwd()
path_to_datasets = cwd + "/cleaned_datasets/"
files_in_folder = os.listdir(path_to_datasets)
files_in_folder.sort()
df_path = path_to_datasets + files_in_folder[0]
df_data = pd.read_csv(df_path, sep="\t")
st.dataframe(df_data, use_container_width=True)

st.write(df_data.dtypes, use_container_width=True)


st.markdown("###")
# st.markdown("""ESeyes only: This exploration strategy involves only using the eyes to gather information about the environment. This can include looking at the layout of the environment, the appearance of objects, and any other visual cues that might be present.

# EStext: This exploration strategy involves reading any text that is present in the environment. This can include labels, instructions, or other written information that might be useful in understanding the environment.

# ESopportunistic: This exploration strategy involves taking advantage of any opportunities that present themselves while exploring the environment. This might include interacting with objects or using available resources in a creative way.

# ESentry: This exploration strategy involves identifying and using specific entry points or starting points for exploration. This might include starting at a particular location or using a specific tool or resource to begin the exploration process.

# ESstructure: This exploration strategy involves examining the structure or organization of the environment, including the relationships between different objects and the overall layout of the space.

# ESpermutations: This exploration strategy involves trying different combinations or permutations of actions or interactions in order to explore the environment. This might involve trying different combinations of tools or resources, or trying different sequences of actions.

# ESleverage: This exploration strategy involves using familiar knowledge or skills to inform the exploration process. This might involve applying knowledge or techniques from previous experiences or using familiar tools or resources in a new context.""")
