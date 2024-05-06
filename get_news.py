import streamlit as st
import yfinance as yf
import json

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
        # Fetch and display news
        news_data = stock.news
        if not news_data:
            st.write(f"No recent news available for {stock_symbol.upper()}.")
        else:
            st.write(f"**Latest news for {stock_symbol.upper()}**")
            for news in news_data:
                try:
                    # Ensure that individual news items conform to JSON
                    formatted_news = json.loads(json.dumps(news))  # Converts back and forth for double-checking
                    st.write(f"- [{formatted_news['title']}]({formatted_news['link']}) - Published by {formatted_news['publisher']}")
                except json.JSONDecodeError:
                    st.write("Warning: Skipping malformed news item.")

    except json.JSONDecodeError as e:
        st.error(f"Unable to fetch news for {stock_symbol.upper()} due to JSON error: {str(e)}")
    except Exception as e:
        st.error(f"Unable to fetch news for {stock_symbol.upper()}: {str(e)}")
