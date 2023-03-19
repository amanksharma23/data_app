import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly

st.set_page_config(layout="wide")

analysis_col, settings_col = st.columns((4, 1))

analysis_col.title("Analysis :chart_with_upwards_trend:")

settings_col.title("Settings :gear:")

uploaded_file =  settings_col.file_uploader("Choose File")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    ##def preprocessing(df):
       ## x = pd.DataFrame()
       ## y = pd.DataFrame()
    df['Date'] = df['Date'].astype('datetime64')

        ##for i in df.columns:

            ##if df[i].dtype == np.dtype('datetime64[ns]'):
                ##x = pd.concat([y,df[i]], axis=1)
                    
            ##elif df[i].dtype == np.dtype('float64') or df[i].dtype == np.dtype('int64'):
                ##y = pd.concat([y,df[i]], axis=1) 

        ##past_data = pd.concat([x,y], axis = 1)

        ##return past_data,list(past_data.columns)


    final_data, past_data_cols = df,list(df.columns)

    categorical_col = settings_col.selectbox("Select the dimension", options= past_data_cols)
    target_col = settings_col.selectbox("Select the metric", options= past_data_cols)
    trend_analysis = settings_col.selectbox("Select the metric for trend analysis", options=past_data_cols, index=0)


    analysis_col.plotly_chart(px.bar(data_frame=final_data,x=categorical_col, y = target_col, template='ggplot2', height = 500), use_container_width=True)
    analysis_col.plotly_chart(px.line(data_frame=final_data,x=final_data['Date'], y = trend_analysis,title="Trend analysis", template='seaborn', height = 500), use_container_width=True)


else:
    analysis_col.header("Please upload a .csv file")

