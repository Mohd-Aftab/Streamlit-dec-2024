import streamlit as st
import yfinance as yf
import datetime

st.title("Stock price analysis")

stock_name = st.text_input("Which stock do you want to analyse", "MSFT")
ticker_data = yf.Ticker(stock_name)

start_date = st.date_input("Please enter starting date", datetime.date(2023,12,1))
end_date = st.date_input("Please enter end date", datetime.date(2024,12,1))


ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

st.subheader("Here is the raw day wise stock price")
st.dataframe(ticker_df.head())

st.subheader("Price movement over time")
st.line_chart(ticker_df['Close'])

st.subheader("Volume movement over time")
st.line_chart(ticker_df['Volume'])