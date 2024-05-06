import streamlit as st
import yfinance as yf

# Default stock symbol
default_symbol = "MSFT"

# Streamlit form to input a stock symbol
st.title("Yahoo Finance Stock News")
with st.form(key="stock_form"):
    stock_symbol = st.text_input("Enter Stock Symbol", value=default_symbol)
    submit_button = st.form_submit_button(label="Fetch News")

# Fetch stock data and news only when the form is submitted
if submit_button:
    stock = yf.Ticker(stock_symbol)

    try:
        # Attempt to fetch news
        news_data = stock.news
        if news_data:
            st.write(f"**Latest news for {stock_symbol.upper()}**")
            for news in news_data:
                st.write(f"- [{news['title']}]({news['link']}) - Published by {news['publisher']}")
        else:
            st.write(f"No recent news available for {stock_symbol.upper()}.")
    except ValueError as e:
        st.error(f"Error processing JSON data: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
