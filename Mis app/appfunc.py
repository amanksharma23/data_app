import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def preprocessing(df):
    df = df.dropna(subset = ['Expiry Date'])
    df['Expiry Date'] = pd.to_datetime(df['Expiry Date'])
    df['Created On'] = pd.to_datetime(df['Created On'])
    df['today'] = pd.datetime.today().strftime('%Y-%m-%d')
    df['expiry days'] = (pd.to_datetime(df['Expiry Date']) - pd.to_datetime(df['today']) ).dt.days.astype(int)

    bins = [-10000,-1,30,60,90,120,150,2000]
    labels = ['Already expired','0-30 days', '31-60 days', '61-90 days', '91-120 days', '120-150 days', '150+ days']
    df['Expiry'] = pd.cut(df['expiry days'], bins, labels=labels)


    df1 = df.iloc[:,:7]
    df2 = df[df.columns[-2:]]
    final_df = pd.concat([df1,df2], axis =1)


    metrics = []
    dimensions = []

    for i in df.columns:
        if df[i].dtype == np.dtype('int64') or df[i].dtype == np.dtype('float64'):
            metrics.append(df[i])
        elif df[i].dtype != np.dtype('datetime64[ns]') or df[i].dtype != np.dtype('int64') or df[i].dtype != np.dtype('float64'):
            dimensions.append(df[i])
        else:
            dimensions = []
 

    if len(dimensions) == 0:
        dimensions_data = pd.DataFrame()
    else:
        dimensions_data = pd.concat(dimensions,axis=1)

    if len(metrics) == 0:
        metrics_data = pd.DataFrame()
    else:
        metrics_data = pd.concat(metrics,axis=1)
  
    if len(list(metrics_data.columns)) <=2 and len(list(metrics_data.columns)) >0:
        metrics_data = pd.concat([metrics_data,dimensions_data],axis=1)
    else:
        metrics_data

    return final_df, final_df.columns, list(final_df['Expiry'].unique()),list(metrics_data.columns), list(dimensions_data.columns)