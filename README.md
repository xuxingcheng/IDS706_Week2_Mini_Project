# Gold Price Prediction

## Project overview

This beginner-friendly project analyzes daily market data from 2015 through August 2025. The dataset contains values for the S&P 500 (SPX), gold (GLD), oil (USO), silver (SLV), and the euro-to-dollar exchange rate (EUR/USD). The main goal is to practice basic Pandas analysis and begin exploring machine learning.

## Dataset

The analysis uses gold_data_2015_25.csv. It contains 2,666 daily observations and six original columns. The Date column is converted to a date, and a Year column is created for grouping.

## Steps

1. Imported Pandas, NumPy, and Matplotlib.
2. Loaded the CSV file with pd.read_csv().
3. Inspected the data with head(), info(), and describe().
4. Checked for missing values and duplicate rows.
5. Filtered rows where GLD is above its overall average.
6. Grouped the data by year and calculated the mean and count of GLD values.
7. Created a line plot of average GLD price by year.
8. Used linear regression to predict GLD from SPX, USO, SLV, and EUR/USD.
9. Evaluated the model with mean absolute error and R-squared.
10. Created a simple year-based linear regression plot for 2025 through 2050.

## Findings

- The dataset has no missing values and no duplicate rows.
- The overall average GLD value is about 158.60.
- There are 1,299 days with a GLD value above the overall average.
- The yearly average rises from about 111.15 in 2015 to about 288.87 in the available 2025 data.
- The 2025 count is lower because the dataset ends in August 2025.
- The linear regression test mean absolute error is about 9.77.
- The model R-squared is about 0.907 on the randomly selected test rows.

## Model limitations

This model is only a first experiment. A strong score on randomly selected historical rows does not guarantee accurate future predictions. The relationships can change over time, and the model does not prove that any input causes changes in gold prices.

The 2025-2050 plot is a simple extension of the historical trend. It should not be treated as a reliable long-term financial forecast.

## Run the notebook

Open gold_price_prediction.ipynb in Jupyter Notebook or VS Code and run the cells from top to bottom. Keep the CSV file in the same folder as the notebook.

(Assisted by ChatGPT, manually checked all contents created)