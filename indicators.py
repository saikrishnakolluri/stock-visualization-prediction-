import pandas_datareader.data as web
import streamlit as st
import plotly as plt

def moving():
    symbol=st.text_input("enter ticker","AAPL")
    start ="2010-01-01"
    end="2022-04-16"
    df=web.DataReader(symbol,"yahoo",start,end)
    st.subheader("Data from 2010-2022")
    st.write(df.describe())
    
    st.subheader(f"closing price vs time chart")
   
    ma100=df.Open.rolling(100).mean()
    fig=plt.figure(figsize=(12,6))
    plt.plot(df.Close)
    plt.plot(ma100,'r',label="Open")
    st.pyplot(fig)