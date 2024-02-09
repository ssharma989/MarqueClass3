# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:32:15 2024

@author: sharm
"""

import streamlit as st
import pandas as pd 
import plotly.express as px 

df = pd.read_csv('AAPL.csv', parse_dates=['Date'], index_col=['Date'])
fig = px.line(df, y='Adj Close')
st.title("DEMO APP - Schulich Class")
st.write(df) #print 
st.plotly_chart(fig)
