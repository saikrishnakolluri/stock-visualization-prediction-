import sample as fed
import yfinance as yf
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import datetime as dt
import time
import patterns as p
import lottie as l
from PIL import Image
from dash.exceptions import PreventUpdate
import sqlite3
import visualize as sai
import forecasting as fore
conn=sqlite3.connect('pd.db')
c=conn.cursor()
def delete(r):
    c.execute('DELETE FROM userstable WHERE username=?',[r])
    conn.commit()
def personal(r):
    all_users=profile(r)
    db=pd.DataFrame(all_users,columns=["Username","Password","Email","Phno","GENDER"])
    st.markdown("Given Details are")
    st.write(db.loc[db['Username'] == r])
@st.cache(suppress_st_warning=True)   
def forecast(n_days, val):
    if val == None:
        raise PreventUpdate
    fig,r = fore.prediction(val, int(n_days) + 1)
    return fig ,r   
def profile(r):
    c.execute(f'SELECT * FROM userstable')
    dat=c.fetchall()
    return dat
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS "userstable" ( "username" TEXT UNIQUE, "password" TEXT NOT NULL, "email" TEXT NOT NULL, "phno" TEXT NOT NULL, "sex" TEXT NOT NULL, PRIMARY KEY("username","email") )')
def add_userdata(username,password,email,phno,sex):#
    c.execute('INSERT INTO userstable(username,password,email,phno,sex) VALUES (?,?,?,?,?)',(username,password,email,phno,sex))    
    conn.commit()
def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data=c.fetchall()
    return data
def admin_user(username,password):
    c.execute('SELECT * FROM admin WHERE username =? AND password = ?',(username,password))
    data=c.fetchall()
    return data    
def view_all_users():
    c.execute('SELECT * FROM userstable')
    data=c.fetchall()
    return data
def viewadmin():
    c.execute('SELECT * FROM admin')
    data=c.fetchall()
    return data
image = Image.open('images.jpg')
st.set_page_config(
     page_title="SAA'S Prediction",
     page_icon=image,
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )
st.title("SAA'S Prediction") 
with st.sidebar:
    st.markdown("<h3 style='color:blue'>WELCOME TO SAA'S WEB-APP</h3>",unsafe_allow_html=True)
    opt=st.selectbox("SERVICES",
    options=['ABOUT US','LOGIN','SIGN UP','VISUALIZE THE STOCK']
    )
if opt=="LOGIN":
    place=st.empty()
    st.sidebar.subheader("Login Section")
    #l.lot("welcom.json")
    username=st.sidebar.text_input("User Name")
    password=st.sidebar.text_input("Password",type='password',)   
    if st.sidebar.checkbox("Login"):
        create_usertable()
        res=login_user(username,password)
        ad=admin_user(username,password)
        if res or ad:
            st.balloons()
            with place.container():
                st.success("Successful Log-in ")
                #st.subheader(f"Welcome {username}!!..",)
                time.sleep(2)
            place.empty()   
            if ad : 
                opt=option_menu(menu_title=None,
                options=['PROFILE','VISUALIZATION','PREDICTION','PATTERNS','USERS LIST','INDICATOR'],
                icons=["cast",'graph-up-arrow','bar-chart-fill','info-circle','people-fill'],
                orientation="horizontal"    )
            else:   
                opt=option_menu(menu_title=None,
                options=['Profile','VISUALIZATION','PREDICTION','PATTERNS',"INDICATOR"],
                icons=["cast",'graph-up-arrow','bar-chart-fill','info-circle','people-fill'],
                orientation="horizontal"    ) 
            if opt =="USERS LIST":
                st.header("USERS")
                all_users=view_all_users()
                all=viewadmin()
                db,admin1=pd.DataFrame(all_users,columns=["Username","Password","Email","Phno","GENDER"]),pd.DataFrame(all,columns=["Username","Password","Email","Phno","GENDER"])
                st.write(db)
                with st.expander('Delete the User Account'):
                    w=st.text_input('Enter user name')
                    w1=st.text_input('Enter Phno')
                    if st.button("Delete the Account"):
                        delete(w) 
                        st.success(f"Successfully deleted the `{w}` Account and Refresh the Page")
                        
                
                st.markdown("<h2 style='color:red'>Admins</h2>",unsafe_allow_html=True)
                st.write(admin1)
            elif opt=="VISUALIZATION":
                st.subheader(
                        'Query parameters to Visualize the stock')
                start_date = st.date_input("Start date", dt.date(2021, 1, 1))
                end_date = st.date_input("End date", dt.date.today())
                st.warning("for NSE STOCKS USE [SYMBOL+.NS]")
                tickerSymbol = st.text_input('ENTER STOCK CODE','RELIANCE.NS')  
                sai.visualize(tickerSymbol,start_date,end_date)
            elif  opt=="PREDICTION":
                x=st.text_input("ENTER THE STOCK CODE","TCS.NS") 
                y=st.number_input("No of days of prediction",5,max_value=30,step=2)
                fig,pre=forecast(y,x)
                tickerData = yf.Ticker(x)
                string_logo = '<img src=%s>' % tickerData.info['logo_url']
                st.markdown(string_logo, unsafe_allow_html=True)
                string_name = tickerData.info['longName']
                st.header('**%s**' % string_name)
                st.plotly_chart(fig)
                sin=pre[len(pre)-1]-pre[0]
                roi=(sin/pre[0])*100
                roi="{:.2f}".format(roi)
                st.subheader("Return of Investment in `%`")
                st.info(roi)

            elif opt=="PROFILE":
                st.success(f"""Welcome back  {username}

                       '{username}' One of the Admin 
                             """)
                st.info("check the services ")
                st.markdown("<h1 style='color:red'>Disclaimer</h1>",unsafe_allow_html=True)    
                st.warning("Trading in Stock Market, Currency or Commodity markets is risky and there is every chance of losing money. One should only trade with a small portion of his or her money which he can afford to lose. Never put all your money in trading and never borrow money to trade." )    
                st.warning("You are requested to check the content with the respective exchanges and see if the contracts are traded there or not as we might have updated our content long time back. Our content on commodities was updated around 10 years ago and the same has been copied here as we have made the new site in wordpress. So please do check the content.")
                st.warning("Our web-app is done for purpose of 'Project' not to provide 'Predictions' of 'Stock prices'")   
                #r=username
                #personal(r) 
                #if st.button("Delete My Account"):
                  #delete(username)      
            elif opt=="Profile":
                st.success(f"Welcome back {username}")
                st.info("check the services ")
                st.markdown("<h1 style='color:red'>Disclaimer</h1>",unsafe_allow_html=True)    
                st.warning("Trading in Stock Market, Currency or Commodity markets is risky and there is every chance of losing money. One should only trade with a small portion of his or her money which he can afford to lose. Never put all your money in trading and never borrow money to trade." )    
                st.warning("You are requested to check the content with the respective exchanges and see if the contracts are traded there or not as we might have updated our content long time back. Our content on commodities was updated around 10 years ago and the same has been copied here as we have made the new site in wordpress. So please do check the content.")
                st.warning("Our web-app is done for purpose of 'Project' not to provide 'Predictions' of 'Stock prices'")   
                r=username
                personal(r) 
                if st.button("Delete My Account"):
                    delete(username)         
            elif opt=='PATTERNS':
                p.patterns()    
            elif opt=="INDICATOR":
                p.moving()
        else:
            st.warning("INVALID CREDENTIALS..!!!..") 
            st.info("Use SIGN UP Option to Create an Account")
elif opt=="SIGN UP":
    with st.sidebar:
        l.lot("signup.json")
    st.subheader('Create New Account')
    create_usertable()
    new_user=st.text_input('Username')
    new_password=st.text_input('Pass-word',type='password')
    confirm=st.text_input("Re-enter Password",type='password')
    email=st.text_input("Enter your Email-id")
    phno=st.text_input("Enter Contact No",max_chars=10)
    sex=st.selectbox("Select Gender",options=["M","F"])
    all_users=profile(new_user)
    db=pd.DataFrame(all_users,columns=["Username","Password","Email","Phno","GENDER"])
    
    if 'key' not in st.session_state:
      st.session_state['key'] = 'value'
    
    if st.button("Signup"):
        if new_user =="" and new_password=="" :
            st.warning("Please Enter the Details")
        elif new_user==new_password:
            st.warning("username and password should not match")    
        elif len(new_password)<6:
            st.warning("Please choose a password of minimum of 6 characters")
        elif confirm!=new_password :
            st.warning("Re-entered password did not match with entered password")   
        else:        
            create_usertable()
            add_userdata(new_user,new_password,email,phno,sex)
            st.success("Successfully Created a New Account in Saa's")
            st.info("Use `LOGIN` option to SIGN-IN ")
            st.balloons()
elif opt=="VISUALIZE THE STOCK":
    st.image(image,width=125)  
    st.markdown("<h3 style='color:ORANGE'>SAA'S VISUALIZATION</h3>",unsafe_allow_html=True)
    st.sidebar.subheader(
        'Query parameters to Visualize the stock')
    start_date = st.sidebar.date_input("Start date", dt.date(2021, 9, 18))
    end_date = st.sidebar.date_input("End date", dt.date.today())
    st.sidebar.warning("for NSE STOCKS USE [SYMBOL+.NS]")
    tickerSymbol = st.sidebar.text_input('ENTER STOCK CODE','aapl')
    sai.visualize(tickerSymbol,start_date,end_date)
elif opt=="ABOUT US":
    with st.sidebar:
        l.lot("top.json")
    sai.about()
    fed.feedback()
    