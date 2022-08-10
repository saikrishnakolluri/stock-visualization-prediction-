from streamlit_lottie import st_lottie
import streamlit as st
import json
def lot(p):
    def load_lottiefile(file: str):
        with open(file,"r") as f:
            return json.load(f)
    t=load_lottiefile(p)     
    st_lottie(t)   