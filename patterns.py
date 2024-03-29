import streamlit as st
import yfinance as yf
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from PIL import Image
def patterns():
    st.subheader("Stocks Information")
    st.markdown("<b>What are Stocks?</b>",unsafe_allow_html=True)
    st.markdown("Stocks are issued by companies to raise capital in order to grow the business or undertake new projects. There are important distinctions between whether somebody buys shares directly from the company when it issues them (in the primary market) or from another shareholder (on the secondary market).")
    st.write(" Stocks are of two types—common and preferred. The difference is while the holder of the former has voting rights that can be exercised in corporate decisions, the later doesn't. However, preferred shareholders are legally entitled to receive a certain level of dividend payments before any dividends can be issued to other shareholders.")
    st.write("There is also something called 'convertible preferred stock'. This is basically a preferred stock with an option of converting into a fixed number of common shares, usually any time after a predetermined date.")
    st.markdown("<b>What are Candlesticks?</b>",unsafe_allow_html=True)
    st.write("Candlesticks are useful when trading as they show four price points (open, close, high, and low) throughout the period of time the trader specifies. Many algorithms are based on the same price information shown in candlestick charts. Trading is often dictated by emotion, which can be read in candlestick charts.")
    image1 = Image.open('candle.jpg')
    image2=Image.open('hammer.png')
    st.image(image1)
    st.markdown("<h2 style='color:green'>Bullish candlestick patterns</h2>",unsafe_allow_html=True)
    st.markdown("<b>1.HAMMER</b>",unsafe_allow_html=True)
    st.image(image2)
    st.write('It indicates a buying pressure, followed by a selling pressure that was not strong enough to drive the market price down. The inverse hammer suggests that buyers will soon have control of the market.')
    st.markdown("<b>2.Bullish engulfing</b>",unsafe_allow_html=True)
    st.write("The bullish engulfing pattern is formed of two candlesticks. The first candle is a short red body that is completely engulfed by a larger green candle.")
    image3=Image.open("bullish-engulfing.png")
    image4=Image.open("Piercingline.png")
    image5=Image.open("morning-star.png")
    image6=Image.open("three-white-soldiers.png")
    image7=Image.open("hanging-man.png")
    image8=Image.open("shooting-star.png")
    image9=Image.open("Doji.png")
    image10=Image.open("spinning-top.png")
    image11=Image.open("falling-three-methods.png")
    st.image(image3)
    st.markdown("<b>3.Piercing line</b>",unsafe_allow_html=True)
    st.write("The piercing line is also a two-stick pattern, made up of a long red candle, followed by a long green candle.")
    st.write("There is usually a significant gap down between the first candlestick’s closing price, and the green candlestick’s opening. It indicates a strong buying pressure, as the price is pushed up to or above the mid-price of the previous day.")
    st.image(image4)
    st.markdown("<b>4.Morning star</b>",unsafe_allow_html=True)
    st.write("The morning star candlestick pattern is considered a sign of hope in a bleak market downtrend. It is a three-stick pattern: one short-bodied candle between a long red and a long green. Traditionally, the ‘star’ will have no overlap with the longer bodies, as the market gaps both on open and close.")
    st.write("It signals that the selling pressure of the first day is subsiding, and a bull market is on the horizon.")
    st.image(image5)
    st.markdown("<b>5.Three white soldiers</b>",unsafe_allow_html=True)
    st.write("It is a very strong bullish signal that occurs after a downtrend, and shows a steady advance of buying pressure.")
    st.image(image6)
    st.markdown("<h2 style='color:red'>Bearish candlestick patterns</h2>",unsafe_allow_html=True)
    st.markdown("<b>1.Hanging man</b>",unsafe_allow_html=True)
    st.write("It indicates that there was a significant sell-off during the day, but that buyers were able to push the price up again. The large sell-off is often seen as an indication that the bulls are losing control of the market.")
    st.image(image7)
    st.markdown("<b>2.Shooting star</b>",unsafe_allow_html=True)
    st.write("The shooting star is the same shape as the inverted hammer, but is formed in an uptrend: it has a small lower body, and a long upper wick.Usually, the market will gap slightly higher on opening and rally to an intra-day high before closing at a price just above the open – like a star falling to the ground.")
    st.image(image8)
    st.markdown("<h2 style='color:orange'>Continuation candlestick patterns</h2>",unsafe_allow_html=True)
    st.markdown("<b>1.Doji</b>",unsafe_allow_html=True)
    st.image(image9)
    st.write("When a market’s open and close are almost at the same price point.This doji’s pattern conveys a struggle between buyers and sellers that results in no net gain for either side. Alone a doji is neutral signal, but it can be found in reversal patterns such as the bullish morning star and bearish evening star.")
    st.markdown("<b>2.Spinning top</b>",unsafe_allow_html=True)
    st.write("The spinning top candlestick pattern has a short body centred between wicks of equal length. The pattern indicates indecision in the market, resulting in no meaningful change in price: the bulls sent the price higher, while the bears pushed it low again. Spinning tops are often interpreted as a period of consolidation, or rest, following a significant uptrend or downtrend.")
    st.image(image10)
    st.markdown("<b>3.Falling three methods</b>",unsafe_allow_html=True)
    st.write("Three-method formation patterns are used to predict the continuation of a current trend, be it bearish or bullish.")
    st.image(image11)
#@st.cache(suppress_st_warning=True)
def moving():
    symbol=st.text_input("Enter Stock code","AAPL")
    tickerData = yf.Ticker(symbol)
    string_logo = '<img src=%s>' % tickerData.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)
    string_name = tickerData.info['longName']
    st.header('**%s**' % string_name)
    start ="2010-01-01"
    end="2022-04-16"
    df=web.DataReader(symbol,"yahoo",start,end)
    st.subheader("Data from 2010-2022")
    st.write(df.describe())

    st.subheader(f"Closing price vs time chart")
    ma100=df.Open.rolling(100).mean()
    fig=plt.figure(figsize=(10,5))
    plt.plot(df.Close)
    plt.plot(ma100,'r',label="Open")
    st.pyplot(fig)    

    st.subheader(f"Open price vs time chart")
    ma100=df.Open.rolling(200).mean()
    fig=plt.figure(figsize=(10,5))
    plt.plot(df.Open)
    plt.plot(ma100,'r',label="Open")
    st.pyplot(fig)  

      