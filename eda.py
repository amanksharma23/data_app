import streamlit as st
import time
import pandas as pd
import numpy as np
import plotly.express as px
from edafunc import preprocessing
from edafunc import pca_maker

st.set_page_config(layout="wide")


logo,row0_1,row0_2,name_spc = st.columns((.5,2.5, 1,1))
with logo:
    st.image('logo2.png', width=100)
with row0_1:
    st.title('Exploratory Data :blue[Analysis] Tool')
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
    
def load_data():
            df = pd.read_csv('app_category_dataset.csv')
            return df

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    with st.spinner('Wait for it...'):
        time.sleep(1)

    df1,dfrs2 = st.columns((2.5,2.5))
    
    with df1:
        st.subheader(":blue[Data]frame")
        df1.dataframe(df)

    with dfrs2:
        st.subheader("Correlation :blue[Matrix]")
        correlation = df.corr()
    
    dfrs2.plotly_chart(px.imshow(correlation,template='plotly' ,text_auto=True))
        
    
    metrics, dimensions, dates, category = preprocessing(df)
    pca_data, pca_cols = pca_maker(df)

    
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

    trend,row_spc1,row_spc2 = st.columns((2.5,1.5,1))
    with trend:
        st.subheader("Trend :blue[Analysis]")
    trend1,trend2 = st.columns((1.5,1.5))
    
    with row_spc1:
        date_trend2 =  st.selectbox("Select the date column for trend analysis", options= dates)
    with row_spc2:
        metric_trend1 =  st.multiselect("Select the metric for trend analysis", options= metrics,default=metrics[:2])

    trend2,row_spc21 = st.columns((4.9,.1))

    bar.plotly_chart(px.histogram(data_frame=df,x=categorical_col, y = metric_col,template='plotly', height = 500,text_auto = True), use_container_width=True)
    pie.plotly_chart(px.pie(data_frame=df,values=metric_piecol,names=categorical_piecol, height=500))
    trend2.plotly_chart(px.line(data_frame=df,x=date_trend2, y = metric_trend1, template='plotly', width = 1200,height = 500), use_container_width=False)

    pca, pca_rs = st.columns((3.5,1.5))
    with pca:
        st.subheader("Principle Component :blue[Analysis]")
    with pca_rs:
        st.title("")
        st.title("")
        cat_col = pca_rs.selectbox("Select Dimensions", options= category)
        pca_1 = pca_rs.selectbox("First Principle Component", options=pca_cols, index=0)
        pca_2 = pca_rs.selectbox("Second Principle Component", options=pca_cols)
            
        pca.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y=pca_2,color=cat_col, template="plotly", height=500, width=500), use_container_width=True)
    


elif row_space.checkbox('Check to use Example Dataset'):
        
        df = load_data()

        with st.spinner('Wait for it...'):
            time.sleep(1)

        df1,dfrs2 = st.columns((2.5,2.5))
        
        with df1:
            st.subheader(":blue[Data]frame")
            df1.dataframe(df)

        with dfrs2:
            st.subheader("Correlation :blue[Matrix]")
            correlation = df.corr()
        
        dfrs2.plotly_chart(px.imshow(correlation,template='plotly' ,text_auto=True))
            
        
        metrics, dimensions, dates, category = preprocessing(df)
        pca_data, pca_cols = pca_maker(df)

        
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

        trend,row_spc1,row_spc2 = st.columns((2.5,1.5,1))
        with trend:
            st.subheader("Trend :blue[Analysis]")
        trend1,trend2 = st.columns((1.5,1.5))
        
        with row_spc1:
            date_trend2 =  st.selectbox("Select the date column for trend analysis", options= dates)
        with row_spc2:
            metric_trend1 =  st.multiselect("Select the metric for trend analysis", options= metrics,default=metrics[:2])

        trend2,row_spc21 = st.columns((4.9,.1))

        bar.plotly_chart(px.histogram(data_frame=df,x=categorical_col, y = metric_col,template='plotly', height = 500,text_auto = True), use_container_width=True)
        pie.plotly_chart(px.pie(data_frame=df,values=metric_piecol,names=categorical_piecol, height=500))
        trend2.plotly_chart(px.line(data_frame=df,x=date_trend2, y = metric_trend1, template='plotly', width = 1200,height = 500), use_container_width=False)

        pca, pca_rs = st.columns((3.5,1.5))
        with pca:
            st.subheader("Principle Component :blue[Analysis]")
        with pca_rs:
            st.title("")
            st.title("")
            cat_col = pca_rs.selectbox("Select Dimensions", options= category)
            pca_1 = pca_rs.selectbox("First Principle Component", options=pca_cols, index=0)
            pca_2 = pca_rs.selectbox("Second Principle Component", options=pca_cols)
                
            pca.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y=pca_2,color=cat_col, template="plotly", height=500, width=500), use_container_width=True)
