import streamlit as st
import pandas as pd
import plotly.express as px
from app_functions import pca_maker


st.set_page_config(layout="wide")

analysis_col, settings_col = st.columns((4, 1))

analysis_col.title("Analysis")

settings_col.title("Settings")

uploaded_file =  settings_col.file_uploader("Choose File")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_cols =  pca_maker(df) 

    categorical_variable = settings_col.selectbox("Variable Select", options = cat_cols)
    categorical_variable_2 = settings_col.selectbox("Second Variable Select", options = cat_cols)
    
    pca_1 = settings_col.selectbox("First Principle Column", options = pca_cols, index=0)
    pca_cols.remove(pca_1)
    pca_2 = settings_col.selectbox("Second Principle Column", options = pca_cols, index=0)

    analysis_col.plotly_chart(px.scatter(data_frame=pca_data, x= pca_1, y=pca_2, color=categorical_variable, template='streamlit', height = 700), use_container_width=True)

else:
    analysis_col.header("Please upload a .csv file")