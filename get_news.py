import streamlit as st
import yfinance as yf

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Stock News Dashboard",
    layout="wide"
)

st.title('Stock News Dashboard')

# Function to display news for the specified stock ticker
def display_stock_news(ticker):
    stock = yf.Ticker(ticker)
    
    try:
        # Retrieve news related to the stock
        stock_news = stock.news
        
        # Check if news is available
        if not stock_news:
            st.warning(f"No news available for {ticker}.")
            return
        
        # Display each news item
        st.subheader(f"Latest News for {ticker}")
        for news in stock_news:
            st.write(f"**{news.get('title', 'No title available')}**")
            st.write(f"Publisher: {news.get('publisher', 'No publisher available')}")
            st.write(f"[Read More]({news.get('link', '#')})")
            date = news.get('providerPublishTime', None)
            if date:
                from datetime import datetime
                date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
            st.write(f"Date: {date if date else 'No date available'}")
            st.markdown("---")
    except Exception as e:
        st.error(f"Failed to load stock news: {e}")

# Input field to provide the stock ticker
ticker = st.text_input('Enter Stock Ticker', 'AAPL')

# Fetch and display the news for the specified ticker
if ticker:
    display_stock_news(ticker)
