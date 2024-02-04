import streamlit as st
import requests
import pandas as pd
import time

def colorFn(v):
    if v.name == 'Buy':
        return ['color: deepSkyBlue'] * len(v)
    if v.name == 'Sell':
        return ['color: red'] * len(v)
    
mode = st.selectbox(
        "",
        ("Lock","Dry", "Market Data"),
)

with st.empty():
   
    while mode == 'Lock':
        data = requests.get("http://127.0.0.1:8000/options/").json()
        df = pd.DataFrame(data['excerpt']['lockData'], columns=['Profit Price','Buy','Sell','Index'])
        df = df.style.apply(colorFn, subset=(slice(None),['Buy','Sell'])
        ).applymap(lambda x: 'color: lime' if float(x) <= 0.25 else None, subset=(slice(None),['Index']))
        st.dataframe(df, hide_index=True, width=800, height=330)
        time.sleep(10)
        
    while mode == "Dry":
        # Apply custom styles to the entire Streamlit app
        data = requests.get("http://127.0.0.1:8000/options/").json()
        df = pd.DataFrame(data['excerpt']['dryData'], columns=['Strike','Buy', 'Price']).style.apply(
        colorFn, subset=(slice(None),['Buy']))
        st.dataframe(df, hide_index=True, width=900, height=330)
        time.sleep(10)
    while mode == "Market Data":
        data = requests.get("http://127.0.0.1:8000/options/").json()
        df = pd.DataFrame(data['excerpt']['optionsData'])
        st.dataframe(df, hide_index=True, width=900, height=330)
        time.sleep(10)