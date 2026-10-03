
# Google Play Store Analytics

## Project Overview

This project explores the Google Play Store dataset to identify patterns and business insights related to app categories, ratings, installations, pricing models, user reviews, and update trends.

The analysis follows a complete data analytics workflow, from data cleaning and feature engineering to exploratory data analysis, visualization, and automated report generation.

## Objectives

- Analyze the distribution of apps across different categories.
- Examine app ratings and installation patterns.
- Compare free and paid applications.
- Explore the relationship between user reviews and installations.
- Identify meaningful trends and business insights.
- Present findings through visualizations and a PDF report.

## Project Workflow

1. **Data Loading:** Import and inspect the Google Play Store dataset.
2. **Data Preprocessing:** Handle missing values, duplicates, invalid records, and data type conversions.
3. **Feature Engineering:** Create additional analytical features, including Year, Month, Is_Paid, Install_Category, and Price_Category.
4. **Exploratory Data Analysis:** Investigate categories, ratings, installs, pricing, reviews, and update trends.
5. **Business Insights:** Extract meaningful findings from the analysis.
6. **Business Recommendations:** Provide data-driven recommendations based on the findings.
7. **Automated Reporting:** Generate a PDF report containing key insights and visualizations.

## Key Findings

- FAMILY is the largest app category by number of records.
- GAME has the highest total installations.
- EVENTS has the highest average app rating.
- Free applications significantly outnumber paid applications.
- Free apps have higher average installations, while paid apps have a slightly higher average rating.
- Reviews and installations show a moderate positive correlation of approximately 0.635.
- 2018 contains the highest number of records by last update year.

## Visualizations

The project includes seven visualizations covering category distribution, ratings, installations, pricing, user engagement, and update trends.

See the [Plots Folder](plots/) for all charts and their descriptions.

## Project Structure

```text
Task_5_Google_Play_Store_Analytics/
│
├── plots/
│   ├── Apps by Year.png
│   ├── Average Rating by Category.png
│   ├── Category Distribution.png
│   ├── Free vs Paid Apps.png
│   ├── Installs by Category.png
│   ├── Rating Analysis.png
│   └── Reviews vs Installs.png
│
├── Google_Play_Store_Analytics.ipynb
├── Google_Play_Store_Analytics_Report.pdf
├── googleplaystore.csv
└── README.md
```

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- ReportLab
- Google Colab

## Dataset

**Source:** [Google Play Store Apps Dataset – Kaggle](https://www.kaggle.com/datasets/lava18/google-play-store-apps)

## Project Deliverables

- Jupyter Notebook containing the complete analysis.
- Seven data visualizations.
- Automated PDF analytics report.
- Project documentation.

## Conclusion

This project demonstrates the application of Python-based data analytics techniques to a real-world app marketplace dataset. It transforms raw application data into meaningful visualizations, business insights, and recommendations.

