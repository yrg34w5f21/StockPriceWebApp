# Import necessary libraries
import streamlit as st  # Streamlit for building web applications
import yfinance as yf  # yfinance for downloading stock data
import pandas as pd  # Pandas for data manipulation
import plotly.express as px  # Plotly Express for interactive plotting

# Set the title of the web page
st.title('Google Stock Price Analysis')

# Sidebar for user input
st.sidebar.header('Date Range Selection')  # Create a sidebar with a header for date selection

# Default start and end dates for user input
start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2019-01-01'))  # Date input for start date
end_date = st.sidebar.date_input('End Date', pd.to_datetime('2022-12-31'))  # Date input for end date

# Get Google stock data from Yahoo Finance
ticker = 'GOOGL'  # Stock symbol for Google
data = yf.download(ticker, start=start_date, end=end_date)  # Download historical stock data

# Display the raw data
st.subheader('Raw Stock Price Data')  # Subheader for raw data section
st.write(data)  # Display the raw stock price data in a table

# Resample data based on user selection (daily, monthly, yearly)
resample_frequency = st.sidebar.radio('Select Time Frequency', ['D', 'M', 'Y'])  # Radio button for frequency selection
resampled_data = data['Close'].resample(resample_frequency).mean()  # Resample closing prices based on user's choice

# Plot the closing prices
st.subheader(f'Closing Price Chart ({resample_frequency} frequency)')  # Subheader for closing price chart
fig = px.line(resampled_data, x=resampled_data.index, y=resampled_data.values, labels={'x': 'Date', 'y': 'Closing Price'})
# Create an interactive line chart using Plotly Express
st.plotly_chart(fig)  # Display the chart

# Display additional information
st.subheader('Statistics')  # Subheader for statistics section
st.write(f"Maximum Closing Price: {data['Close'].max()}")  # Display maximum closing price
st.write(f"Minimum Closing Price: {data['Close'].min()}")  # Display minimum closing price
st.write(f"Average Closing Price: {data['Close'].mean()}")  # Display average closing price

# Deployment considerations
st.sidebar.header('Deployment Options')  # Header for deployment options in the sidebar

# Add deployment options here based on specific needs (e.g., saving data or visualizations, deploying to a platform)
# You can customize this section based on your specific requirements
