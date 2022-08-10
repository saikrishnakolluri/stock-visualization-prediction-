import streamlit as st
import pandas as pd
from PIL import Image
import lottie as l
import datetime as dt
import pandas_datareader.data as web
import cufflinks as cf
import yfinance as yf
@st.cache(suppress_st_warning=True)
def visualize(tickerSymbol,start_date,end_date):
    ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
    st.sidebar.markdown("American Stocks")
    st.sidebar.write(ticker_list)
    if tickerSymbol!="":
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            #selected=st.radio("Select the options",options=["STOCK INFO",'STOCK GRAPH','RAW DATA','SHARE HOLDERS'])
            tickerData = yf.Ticker(tickerSymbol) # Get ticker data
            tickerDf = tickerData.history(period='1d', end=end_date, start=start_date) #get the historical prices for this ticker
            tickerDf.reset_index(inplace=True)
            tickerDf['Date'] = pd.to_datetime(tickerDf['Date'],format='%Y-%m-%d')
            tickerDf.sort_values('Date',ascending=True)
            end = dt.datetime.now()
            start = end -dt.timedelta(weeks=52)
            df1 = web.DataReader(tickerSymbol, 'yahoo', start, end)
            high = df1['High'].max()
            low =df1['Low'].min()
            y=len(df1)-1
            y1=df1.Open[y]
            y2=df1.Close[y]
        #if selected=="STOCK INFO":
            string_logo = '<img src=%s>' % tickerData.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)

            string_name = tickerData.info['longName']
            st.header('**%s**' % string_name)
            st.header("Company summary")
            string_summary = tickerData.info['longBusinessSummary']
            st.info(string_summary)
                #elif selected=="RAW DATA":
            st.header('**Stock Raw Data**')
            st.write(tickerDf)
            #st.download_button("Download Raw Data",df1,"Rawdata")
            #st.write(df1) 
                #elif selected=="STOCK GRAPH":
            st.header('**STOCK TRADED GRAPH**')
            qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
            qf.add_bollinger_bands()
            fig = qf.iplot(asFigure=True)
            st.plotly_chart(fig)
                #elif selected=="SHARE HOLDERS"  :
            st.markdown("<h2 style='color:skyblue'>MAJOR HOLDERS</h2>",unsafe_allow_html=True)
            sa=pd.DataFrame(tickerData.major_holders)
            sa.columns=["Percentage","Type"]
            st.write(sa)
            col1, col2 = st.columns(2)
            df=tickerDf
            original = df.Open[0]
            col1.header("Open Price")
            col1.write(y1)
            # grayscale = original.convert('LA')
            #grayscale = df.Close[0]
            col2.header("Prev Close")
            col2.write(y2)
            col6, col7 = st.columns(2)
            col6.header("52 week Low")
            col6.write(low)
            col7.header("52 WEEK HIGH")
            col7.write(high)
            po=((y2-low)/low)*100
            pi=((high-y2)/high)*100
            if po<5:
                st.warning("Stock is trading near to `52 WEEK LOW`")
            if pi<5:
                st.warning("Stock is trading nearer to `52 WEEK HIGH`")    
def about():
    f1,f2=st.columns(2)
    with f2:
        st.markdown('''
        #### SAA'S COMPANY PROFILE
        We are providing all stocks info like `Visualization`, `Prediction` , `CandleSticks patterns` !

        **Credits**
        - App built by `BATCH-007`
        - KOLLURI SAI KRISHNA`(Y19IT059)`
        - CH.ASHISH`(Y19IT014)`
        - D.AKHIL`(Y19IT024)`
        - Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
        
        ''')
    with f1:
        image = Image.open('images.jpg')
        st.image(image,width=125)  
        st.markdown("<h3 style='color:skyblue'>COMPANY LOGO</h3>",unsafe_allow_html=True)
        l.lot("trade.json")

    st.markdown("<h1 style='color:red'>Disclaimer</h1>",unsafe_allow_html=True)    
    st.warning("Trading in Stock Market, Currency or Commodity markets is risky and there is every chance of losing money. One should only trade with a small portion of his or her money which he can afford to lose. Never put all your money in trading and never borrow money to trade." )    
    st.warning("You are requested to check the content with the respective exchanges and see if the contracts are traded there or not as we might have updated our content long time back. Our content on commodities was updated around 10 years ago and the same has been copied here as we have made the new site in wordpress. So please do check the content.")
    st.warning("Our web-app is done for purpose of 'Project' not to provide 'Predictions' of 'Stock prices'")            