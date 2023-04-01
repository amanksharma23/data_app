import streamlit as st
import pandas as pd
from appfunc import preprocessing
import time
import plotly.express as px


st.set_page_config(layout="wide")

row0_1,row0_2 = st.columns((3,2))
with row0_1:
    st.title(':blue[Contracts] Analysis')

fileup,row_space = st.columns((3,2))
with fileup:
    uploaded_file =  st.file_uploader("Choose File")
    

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    with st.spinner('Wait for it...'):
        time.sleep(1)
    
    df,cols,expiry_cols,metric_cols, dimensions =preprocessing(df)

    mulse, mulspc = st.columns((1.5,3.5))
    with mulse:
        st.markdown("")
        st.write("")
        st.subheader("Choose from the :blue[options]")
        choices = st.multiselect("Expiry ageing ",expiry_cols)


    selected_df = df[df['Expiry'].isin(choices)]

    with mulspc:
        st.title("Data:blue[frame]")
        a = st.dataframe(selected_df)



    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(selected_df)
    with mulspc:
        st.download_button(
        "Download Report",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
        )
    barop, barc = st.columns((1.5,3.5))
    with barop:
        st.markdown("")
        st.write("")
        st.subheader("Choose from the :blue[options]")
        cat = st.selectbox("Choose the dimensions", options=dimensions)
        num = st.multiselect("Choose the metrics", options=metric_cols)

    with barc:
        st.title(":blue[Bar] Chart")
        barc.plotly_chart(px.histogram(data_frame=df,x=cat, y = num,template='plotly', height = 500,text_auto = True), use_container_width=True)

else:
    st.subheader("Please upload the :blue[MIS]")