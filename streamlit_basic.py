# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:49:01 2023

@author: Gowtham S
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# dictionary to map coin names to CSV file names
coin_files = {
    'Bitcoin': 'BTC-USD_14-23.csv',
    'Ethereum': 'ETH-USD.csv',
    'DOGE': 'DOGE-USD.csv'
}

# create a dropdown to select the coin
coin = st.selectbox('Select a coin', options=list(coin_files.keys()))

# load the coin data from csv file
df = pd.read_csv(coin_files[coin])


# convert the Date column to datetime data type
df['Date'] = pd.to_datetime(df['Date'])

# set the Date column as the index
df.set_index('Date', inplace=True)

# create a line chart using plotly express
fig = px.line(df, x=df.index, y='Close', title=f'{coin} - USD Time Series')
st.plotly_chart(fig)

# create input fields for investment date and amount
investment_date = st.date_input('Investment Date')
investment_amount = st.text_input('Investment Amount', value='0')

# create a button to trigger the profit/loss calculation
if st.button('Apply'):
    # convert the investment amount to a float
    investment_amount = float(investment_amount)

    # get the current price of bitcoin
    current_price = df.iloc[-1]['Close']

    # calculate the potential profit or loss
    if investment_date > df.index[-1]:
        st.write('Error: Investment date cannot be in the future.')
    else:
        investment_date = pd.Timestamp(investment_date)  # convert to pandas Timestamp object
        investment_price = df.loc[investment_date]['Close']
        investment_value = investment_amount * investment_price
        current_value = investment_amount * current_price
        profit_loss = current_value - investment_value
    
    st.write('Potential Profit:<div style="color: green; font-weight: bold;">The money you would have, enjoy</div>', 
                     unsafe_allow_html=True)
            
    st.write('Potential Loss:<div style="color: red; font-weight: bold;">Money that could be gone, move on</div>', 
                     unsafe_allow_html=True)
    