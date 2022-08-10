import streamlit as st
from PIL import Image
def about():
    f1,f2=st.columns(2)
    with f2:
        st.markdown('''
        # SAA'S ANALYSIS
        Shown are the stock price data for query companies!

        **Credits**
        - App built by BATCH-007
        - KOLLURI SAI KRISHNA(Y19IT059)
        - CH.ASHISH(Y19IT014)
        - D.AKHIL(Y19IT024)
        - Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
        ''')
    with f1:
        image = Image.open('images.jpg')
        st.image(image,width=125)  
        st.markdown("<h3 style='color:skyblue'>COMPANY LOGO</h3>",unsafe_allow_html=True)
    st.markdown("<h1 style='color:red'>Disclaimer</h1>",unsafe_allow_html=True)    
    st.warning("Trading in Stock Market, Currency or Commodity markets is risky and there is every chance of losing money. One should only trade with a small portion of his or her money which he can afford to lose. Never put all your money in trading and never borrow money to trade." )    
    st.warning("You are requested to check the content with the respective exchanges and see if the contracts are traded there or not as we might have updated our content long time back. Our content on commodities was updated around 10 years ago and the same has been copied here as we have made the new site in wordpress. So please do check the content.")
    st.warning("Our web-app is done for purpose of 'Project' not to provide 'Predictions' of 'Stock prices'")