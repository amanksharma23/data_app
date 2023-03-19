import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler


def pca_maker(df):
    numerical_col = []
    categorical_col = []

    for i in df.columns:
        if df[i].dtype == np.dtype('float64') or df[i].dtype == np.dtype('int64'):
            numerical_col.append(df[i])
        else:
            categorical_col.append(df[i])

    numerical_data = pd.concat(numerical_col, axis=1)
    categorical_data = pd.concat(categorical_col, axis=1)  
    numerical_data = numerical_data.apply(lambda x: x.fillna(np.mean(x)))  

    scaler = StandardScaler()

    scaled_val = scaler.fit_transform(numerical_data)

    pca = PCA()

    pca_data =pca.fit_transform(scaled_val)

    pca_data = pd.DataFrame(pca_data)

    new_col = ["PCA_" + str(i) for i in range(1,len(pca_data.columns)+1)]
    col_mapper = dict(zip(list(pca_data.columns),new_col))

    pca_data = pca_data.rename(columns=col_mapper)

    output = pd.concat([df,pca_data], axis = 1)

    return output, list(categorical_data.columns), new_col