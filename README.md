# Python-Numpy_Find-2-Most-Correlated-Stocks

"Using Numpy in Python, find the 2 most correlated stocks out of 6 different ones: ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB'].

Data Preparation: Load the historial daily data of the entire 2018 for the 6 stocks
tks = ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB']
Provided with 6 csv files. 

Retrieve the "Adj Close" column values as the daily prices of each stock: Read the csv file, split the row, split the column and retrieve the "Adj Close" column values and store them into a dictionary.

Part 1: Compute the correlation between any two stocks. Write non-NumPy version code.

Part 2: Write an one line numpy vectorized version of function correlation(x, y) to compute the correlation of two lists x, and y.

Part 3: Compare the run time of both implementations."
