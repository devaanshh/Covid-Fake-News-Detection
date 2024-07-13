import streamlit as st
from model import doUserTesting
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import time
from streamlit_extras.switch_page_button import switch_page

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.title("Fake Free Zone")

data = pd.read_excel('Constraint_Test.xlsx',header=0)

col1,col2=st.columns(2)
with col1:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.markdown("""Lets  predict the news whether it is real or fake.""")
    st.text("")
    st.markdown("""Real news is a reliable source of information that helps us make informed decisions, while fake news is a dangerous weapon that undermines trust and manipulates our beliefs.""")

#     st.text("RAW DATA")
#     st.dataframe(data)
#     st.markdown("""We can predict the news whether it is real or fake from the dataset provided""")
with col2:
    lottie_url3 = "https://assets6.lottiefiles.com/packages/lf20_WKoqF9SE3v.json"
    lottie_3 = load_lottieurl(lottie_url3)

    st_lottie(lottie_3, key="News")
    

v1=st.text_input("Enter the News")

if st.button("Proceed to predict"):
    prediction=doUserTesting(v1)
    st.text("PREDICTIONS ARE")
    st.text(prediction)