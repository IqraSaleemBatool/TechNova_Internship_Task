AAPL Stock Trend Analysis — README
📌 Project Overview
This project performs a comprehensive time-series analysis of Apple Inc. (AAPL) historical stock prices covering the period from May 27, 2015 to May 22, 2020. The analysis explores price trends, trading behavior, seasonality, anomalies, short-term fluctuations, and forecasting using statistical and machine learning models.

The goal is to extract meaningful insights from historical stock data and demonstrate practical time-series analysis techniques.

📂 Dataset
Attribute	Details
File	AAPL.csv
Records	1,258 rows
Columns	14 (after dropping redundant index)
Period	2015-05-27 → 2020-05-22
Symbol	AAPL
Key Columns
date — Trading date (converted to datetime)

open, high, low, close — Daily OHLC prices

volume — Daily trading volume

adjClose, adjHigh, adjLow, adjOpen, adjVolume — Adjusted prices

divCash — Dividend cash value

splitFactor — Stock split factor

🎯 Objectives
Load, clean, and prepare the AAPL stock dataset

Perform exploratory data analysis (EDA)

Analyze overall time-series trends

Investigate seasonality (monthly/yearly patterns)

Detect anomalies in daily returns using the IQR method

Apply moving average smoothing (7-day and 30-day)

Forecast future prices using Prophet and ARIMA

Evaluate and compare forecasting models

Visualize final forecast results

🛠️ Technologies & Libraries
python
pandas          # Data manipulation
numpy           # Numerical operations
matplotlib      # Visualization
prophet         # Forecasting (Facebook Prophet)
statsmodels     # ARIMA modeling
google.colab    # File upload utility
📊 Analysis Workflow
1. Data Loading and Preparation
Upload and load AAPL.csv

Drop the redundant Unnamed: 0 index column

Convert date to datetime and sort chronologically

Check for missing values and duplicates (none found)

2. Exploratory Data Analysis (EDA)
Minimum closing price: $90.34 (2016-05-12)

Maximum closing price: $327.20 (2020-02-12)

Visualized:

Opening vs. closing prices

Closing price distribution

Trading volume over time

Daily price range (High − Low)

Correlation matrix of price variables

Key Finding: OHLC prices are ~99.9% correlated; volume shows weak negative correlation with price.

3. Time Series Trend Analysis
Overall upward trend from ~$130 (2015) to ~$318 (2020)

Daily returns computed via pct_change()

Yearly average closing prices:

Year	Avg Close
2015	117.83
2016	104.60
2017	150.55
2018	189.05
2019	208.26
2020	291.79
4. Seasonality Analysis
Monthly average prices and monthly returns calculated

Strongest average returns in October (+5.30%) and August (+4.53%)

Weakest returns in November (−2.59%) and December (−1.91%)

5. Anomaly Detection (IQR Method)
Q1 = −0.646, Q3 = 0.934, IQR = 1.580

Bounds: [−3.017, +3.304]

89 anomalies detected

Largest gain: +11.98% (2020-03-13)

Largest drop: −12.86% (2020-03-16)

6. Moving Average Analysis
7-day MA: responsive to short-term changes

30-day MA: smoother, reflects broader trend

MA crossover (MA_difference = MA_7 − MA_30) used to gauge momentum

7. Forecasting (Prophet & ARIMA)
Models trained on historical closing prices

Future prices predicted and visualized

8. Model Evaluation
Compared Prophet vs. ARIMA using error metrics (MAE, RMSE)

9. Final Forecast Visualization
Combined historical data with forecasted trends

🔍 Key Insights
AAPL exhibited a strong long-term uptrend despite short-term volatility

Volume spikes align with periods of high market activity

2020 (COVID-19 period) showed extreme volatility with the largest daily swings

Monthly seasonality suggests October and August historically strong

Moving averages confirm bullish momentum, especially in 2019–2020

▶️ How to Run
Open Task_4_Stock_Trend_Analysis.ipynb in Google Colab or Jupyter Notebook

Install required libraries:

bash
pip install pandas numpy matplotlib prophet statsmodels
Upload AAPL.csv when prompted (or place it in the working directory)

Run cells sequentially from top to bottom

Review outputs, plots, and forecast results

📁 Project Structure
text
Task_4_Stock_Trend_Analysis.ipynb   # Main analysis notebook
AAPL.csv                            # Input dataset
README.md                           # Project documentation
⚠️ Disclaimer
This analysis is for educational and research purposes only. It does not constitute financial advice. Stock markets are inherently unpredictable; past performance is not indicative of future results.

👤 Author
Task 4 — Stock Trend Analysis
Time-Series Analysis Project

