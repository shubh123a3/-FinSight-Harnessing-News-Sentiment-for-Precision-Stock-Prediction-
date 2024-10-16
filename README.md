# FinSight: News-Driven Stock Price Prediction

## Overview


https://github.com/user-attachments/assets/997df64b-2d5e-4a2f-9090-92383d72ee8d


FinSight is an advanced stock price prediction model that combines Long Short-Term Memory (LSTM) networks with FinBERT-powered sentiment analysis of financial news. This project aims to enhance the accuracy of stock price forecasts by incorporating the sentiment of relevant news articles, providing a more comprehensive approach to market prediction.

## Features

- Data scraping from financial news websites
- Sentiment analysis using FinBERT
- Stock price data retrieval via yfinance
- LSTM-based price prediction model
- Integration of price data with sentiment scores
- Comparative analysis of models with and without news sentiment

## Installation
bash
git clone https://github.com/shubh123a3/-FinSight-Harnessing-News-Sentiment-for-Precision-Stock-Prediction-.git
cd -FinSight-Harnessing-News-Sentiment-for-Precision-Stock-Prediction-
pip install -r requirements.txt

## Usage

1. Data Preparation:
   - Run the data scraping script to collect financial news
   - Use yfinance to fetch historical stock prices

2. Sentiment Analysis:
   - Process news articles using FinBERT to obtain sentiment scores

3. Model Training:
   - Prepare the dataset by combining price data and sentiment scores
   - Train the LSTM model using the prepared dataset

4. Prediction and Evaluation:
   - Use the trained model to make predictions
   - Evaluate the model's performance using metrics like MAE and R2 score

## Code Structure

The main components of the project are:

1. Data collection and preprocessing
2. Sentiment analysis using FinBERT
3. LSTM model implementation
4. Model training and optimization
5. Performance evaluation and visualization

Key code sections:

python
startLine: 91
endLine: 111

This section imports necessary libraries and downloads NLTK data.

These lines calculate and print the Mean Absolute Error and R2 score of the model.

## Results

The project demonstrates significant improvements in stock price prediction accuracy when incorporating news sentiment:

- LSTM Model with News Sentiment:
  - Mean Absolute Error: 1.81%
  - R2 Score: 0.9810

- LSTM Model without News Sentiment:
  - Mean Absolute Error: 8.15%
  - R2 Score: 0.9682

## Visualization

The project includes various visualizations:
- Stock price prediction plots
- R2 score bar charts
- Comparison plots of models with and without news sentiment

## Future Work

- Implement real-time news sentiment analysis
- Explore additional feature engineering techniques
- Investigate the impact of different time windows for news sentiment
- Develop a user-friendly web interface for predictions

## Contributing

Contributions to FinSight are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FinBERT developers for the sentiment analysis model
- yfinance library for providing easy access to stock data
- The open-source community for various tools and libraries used in this project

## Contact

For any queries or suggestions, please open an issue in the GitHub repository or contact the project maintainers.
