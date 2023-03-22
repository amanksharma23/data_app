import streamlit as st
import pandas as pd
import numpy as np

def preprocessing(df):
    if 'Date' in df.columns:
        df['Date'] = df['Date'].astype('datetime64[ns]')
    else:
        ""
    metrics = []
    dimensions = []
    dates = []
    categorical_data = pd.DataFrame()

    for i in df.columns:
        if df[i].dtype == np.dtype('int64') or df[i].dtype == np.dtype('float64'):
            metrics.append(df[i])  
        elif df[i].dtype == np.dtype('datetime64[ns]'):
            df['Date']=pd.to_datetime(df['Date'], format='%Y-%m-%d')
            df['Month_year'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m')
            df['Year'] = pd.to_datetime(df['Date']).dt.year
            df['Month'] = pd.to_datetime(df['Date']).dt.month
            dates.append(df[['Date','Month', 'Year']])
        elif df[i].dtype != np.dtype('datetime64[ns]') or df[i].dtype != np.dtype('int64') or df[i].dtype != np.dtype('float64'):
            dimensions.append(df[i])
        else:
            dimensions = []

    if len(dates) == 0:
        dates_data = pd.DataFrame()
    else:
        dates_data = pd.concat(dates,axis=1)   
    if len(metrics) == 0:
        metrics_data = pd.DataFrame()
    else:
        metrics_data = pd.concat(metrics,axis=1)

    if len(dimensions) == 0:
        dimensions_data = pd.DataFrame()
    else:
        dimensions_data = pd.concat(dimensions,axis=1)

    categorical_data = pd.concat([dimensions_data,dates_data], axis = 1)
    df = pd.concat([df,dates_data],axis=1)

    return list(metrics_data.columns), list(dimensions_data.columns), list(dates_data.columns),list(categorical_data.columns)
