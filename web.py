import streamlit as st
import requests
import pandas as pd
import time
import ast

def colorFn(v):
    if v.name == 'Buy':
        return ['color: blue'] * len(v)
    if v.name == 'Sell':
        return ['color: red'] * len(v)

with st.empty():
    while True:
        data = requests.get("http://127.0.0.1:8000/options/").json()
        df = pd.DataFrame(ast.literal_eval(data['optData']), columns=['','Buy','Sell','Index']
        )
        df = df.style.apply(
            colorFn, subset=(slice(None),['Buy','Sell'])
        )
        
        st.table(df) 
        time.sleep(10)