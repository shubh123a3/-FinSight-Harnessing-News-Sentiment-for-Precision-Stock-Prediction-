import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load data function (you'll need to implement this based on your actual data)
def load_data():
    # Load your actual data here
    # For this example, I'll use dummy data
    dates = pd.date_range(start='2022-01-01', periods=100)
    actual_prices = np.random.randn(100).cumsum() + 100
    predicted_with_news = actual_prices + np.random.randn(100) * 2
    predicted_without_news = actual_prices + np.random.randn(100) * 4
    return dates, actual_prices, predicted_with_news, predicted_without_news

def main():
    st.title("Stock Price Prediction With sentimental Analysis With Finbert ",'center')

    # Load data
    dates, actual_prices, predicted_with_news, predicted_without_news = load_data()

    # Display the result images
    st.header("Model Prediction Results", 'center')
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("LSTM Model with News")
        result_image_with_news = Image.open("result/With News.png")
        st.image(result_image_with_news, caption="Stock Price Prediction (with News)")

    with col2:
        st.subheader("LSTM Model without News")
        result_image_without_news = Image.open("result/without news.png")
        st.image(result_image_without_news, caption="Stock Price Prediction (without News)")

    # Metrics comparison
    st.header("Model Performance Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("LSTM Model with News Score")
        st.metric("Mean Absolute Error", "1.81%")
        st.metric("R2 Score", "0.9810")

    with col2:
        st.subheader("LSTM Model without News Score")
        st.metric("Mean Absolute Error", "8.15%")
        st.metric("R2 Score", "0.9682")

    # Comparison plot
    st.header("Model Comparison Plot")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, actual_prices, label='Actual Price', color='blue')
    ax.plot(dates, predicted_with_news, label='Predicted (with news)', color='green')
    ax.plot(dates, predicted_without_news, label='Predicted (without news)', color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    st.pyplot(fig)

    # Model improvement
    st.header("Model Improvement")
    improvement_mae = (8.15 - 1.81) / 8.15 * 100
    improvement_r2 = (0.9810 - 0.9682) / 0.9682 * 100
    st.write(f"By incorporating news sentiment, the model achieved:")
    st.write(f"- {improvement_mae:.2f}% reduction in Mean Absolute Error")
    st.write(f"- {improvement_r2:.2f}% improvement in R2 Score")

    # Insights
    st.header("Insights")
    st.write("""
    1. Improved Accuracy: The LSTM model incorporating news sentiment shows a significant reduction in Mean Absolute Error (MAE) from 8.15% to 1.81%. This represents a 77.79% improvement in prediction accuracy.

    2. Better Explanatory Power: The R2 score increased from 0.9682 to 0.9810, indicating that the model with news sentiment explains more of the variance in the stock price data.

    3. Sentiment Impact: The inclusion of news sentiment clearly enhances the model's ability to predict stock prices, suggesting that market sentiment derived from news articles has a measurable impact on stock price movements.

    4. Potential for Real-world Application: Given the substantial improvement in both MAE and R2 score, this model could potentially be valuable for real-world stock price prediction and trading strategies.

    5. Further Research: While the results are promising, it would be beneficial to test the model on different stocks and time periods to ensure consistency and robustness of the improvements.
    """)

if __name__ == "__main__":
    main()