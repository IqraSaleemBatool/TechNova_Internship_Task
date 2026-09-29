# AAPL Stock Trend Analysis

A time-series analysis of Apple Inc. (AAPL) stock prices (May 2015 – May 2020), covering trend analysis, seasonality, anomaly detection, moving averages, and forecasting with Prophet and ARIMA.

---

##  Dataset

- **File:** `AAPL.csv`
- **Records:** 1,258 rows | **Period:** 2015-05-27 → 2020-05-22
- **Columns:** `date`, `open`, `high`, `low`, `close`, `volume`, adjusted prices, `divCash`, `splitFactor`

---

##  Objectives

- Clean and prepare the dataset
- Perform EDA and trend analysis
- Detect seasonality and anomalies
- Apply moving averages (7-day, 30-day)
- Forecast using Prophet and ARIMA
- Evaluate and visualize model results

---

##  Tech Stack

`pandas` · `numpy` · `matplotlib` · `prophet` · `statsmodels`

---

##  Workflow

| Step | Description |
|------|-------------|
| 1 | Load & preprocess data (datetime, sorting, dedup) |
| 2 | EDA — price trends, volume, daily range, correlation |
| 3 | Time-series trend & daily returns |
| 4 | Seasonality — monthly & yearly patterns |
| 5 | Anomaly detection via IQR method |
| 6 | Moving averages (MA_7, MA_30) |
| 7 | Forecasting with Prophet & ARIMA |
| 8 | Model evaluation & comparison |
| 9 | Final forecast visualization |

---

##  Key Findings

- **Overall upward trend:** ~$130 (2015) → ~$318 (2020)
- **Min/Max close:** $90.34 (2016-05-12) / $327.20 (2020-02-12)
- **89 anomalies** detected; largest swing: **+11.98%** and **−12.86%** (March 2020)
- **Strongest months:** October (+5.30%), August (+4.53%)
- **Weakest months:** November (−2.59%), December (−1.91%)
- OHLC prices are ~99.9% correlated; volume weakly negative with price

---

##  How to Run

1. Open the notebook in **Google Colab** or **Jupyter**
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib prophet statsmodels
   ```
3. Upload `AAPL.csv` when prompted
4. Run cells sequentially

---

##  Structure

```
├── Task_4_Stock_Trend_Analysis.ipynb
├── AAPL.csv
└── README.md
```


