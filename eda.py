import streamlit as st
import time
import pandas as pd
import numpy as np
import plotly.express as px
from edafunc import preprocessing


st.set_page_config(layout="wide")
row0_1,row0_2,name_spc = st.columns((3, 1,1))
with row0_1:
    st.title('Welcome to your :blue[Analysis] tool :golf:')
with name_spc:
    st.title("")
    st.markdown(':red[Streamlit App] by [Aman Sharma](https://www.linkedin.com/in/aman-kumar-sharma2000/)')


fileup,row_space = st.columns((2,2))
with fileup:
    uploaded_file =  fileup.file_uploader("Choose File")

with row_space:
    st.title("") 
    st.title("")
    @st.cache_data 
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    sample_data = pd.read_csv('app_category_dataset.csv')
    csv = convert_df(sample_data)
    row_space.download_button(
        label="Download sample data",
        data=csv,
        file_name='app_category_dataset.csv',
        mime='text/csv',
        )
 

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    with st.spinner('Wait for it...'):
        time.sleep(1)
    
    metrics, dimensions, dates, category = preprocessing(df)

    
    bar1,bar2,pie1,pie2 = st.columns((1.5,1.5,1,1))
    bar,pie = st.columns((3,2))

    with bar1:
        categorical_col = bar1.selectbox("Select the dimension", options= category)
    with bar2:
        metric_col = bar2.selectbox("Select the metric", options= metrics)

    with pie1:
        categorical_piecol = pie1.selectbox("Select the names", options= category)
    with pie2:
        metric_piecol = pie2.selectbox("Select the values", options= metrics)

    trend,row_spc1 = st.columns((3,2))
    with trend:
        st.subheader("Trend :blue[Analysis]")
    trend1,trend2 = st.columns((1.5,1.5))
    
    with row_spc1:
        metric_trend1 =  row_spc1.multiselect("Select the metric for trend analysis", options= metrics)

    trend2,row_spc21 = st.columns((4.9,.1))

    bar.plotly_chart(px.histogram(data_frame=df,x=categorical_col, y = metric_col,template='plotly', height = 500,text_auto = True), use_container_width=True)
    pie.plotly_chart(px.pie(data_frame=df,values=metric_piecol,names=categorical_piecol, height=500))
    trend2.plotly_chart(px.line(data_frame=df,x=df['Date'], y = metric_trend1, template='plotly', width = 1200,height = 500), use_container_width=False)
else:
    row0_1.subheader("Please upload a .csv file")
