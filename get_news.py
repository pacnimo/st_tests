import streamlit as st
import yfinance as yf

# Set page configuration with page title, layout, and initial sidebar state
st.set_page_config(
    page_title="Apple Stock News Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "Apple Stock News Dashboard..."}
)

st.title('Apple Stock News Dashboard')

# Display Apple Stock News
def display_apple_stock_news():
    ticker = "AAPL"
    stock = yf.Ticker(ticker)

    try:
        # Retrieve news related to Apple
        stock_news = stock.news

        # Check if the news list is empty
        if not stock_news:
            st.warning("No news available for Apple.")
            return

        # Display each news item in the Streamlit app
        for news in stock_news:
            st.subheader(news.get('title', 'No title available'))  # Get the news headline
            st.write("Publisher:", news.get('publisher', 'No publisher available'))  # Get the news publisher
            st.write("Link:", news.get('link', 'No link available'))  # Provide the link to the full news
            date = news.get('providerPublishTime', None)
            if date:
                from datetime import datetime
                date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
            st.write("Date:", date if date else 'No date available')
            st.markdown("-------------------------------------------------------")
    except Exception as e:
        st.error(f"Failed to load Apple stock news: {e}")

# Call the function to display Apple stock news
display_apple_stock_news()

