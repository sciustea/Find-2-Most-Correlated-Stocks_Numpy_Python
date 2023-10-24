
# Stefana Ciustea
# CS 310 - Assignment 3

# read the csv file, split the row, split the column and 
# retrieve the "Adj Close" column values and store them into a dictionary

import csv

def get_adj_column(filename):
    file = open(filename, 'r')
 
    # creating dictreader object:
    csv_file = csv.DictReader(file)
 
    # creating empty list:
    adj_close_strings = []
 
    for col in csv_file:
        # iterating over each col and append
        # values to empty list
        adj_close_strings.append(col['Adj Close'])
        
    adj_close = []
    
    for value in adj_close_strings:
        # turning strings value into floats
        adj_close.append(float(value))
    
    # returning list
    return adj_close

allprices = {
    "IBM":get_adj_column('IBM.csv'),
    "MSFT":get_adj_column('MSFT.csv'),
    "GOOG":get_adj_column('GOOG.csv'),
    "AAPL": get_adj_column('AAPL.csv'),
    "AMZN":get_adj_column('AMZN.csv'),
    "FB":get_adj_column('FB.csv')
}

# print(allprices)

# Compute the correlation between any two stocks:

import math
import statistics

def get_correlation_numerator(list_x, list_y):
    # calculates the top half of the sample correlation coefficient equation
    mean_x = statistics.mean(list_x)
    mean_y = statistics.mean(list_y)
    if len(list_x) != len(list_y):
        raise ValueError("lists must be the same length")
    sum_of_product = 0
    for i in range(len(list_x)):
        sum_of_product += (list_x[i]-mean_x)*(list_y[i]-mean_y)
    return sum_of_product

def sum_of_correlation_squares(list_n):
    # calculates part of the bottom half of the sample correlation coefficient equation for x and y
    sum_of_corr_sq = 0
    mean_n = statistics.mean(list_n)
    for i in range(len(list_n)):
        sum_of_corr_sq += (list_n[i]-mean_n)**2
    return sum_of_corr_sq
    
def get_correlation(list_x, list_y):
    # calculates the sample correlation coefficient
    correlation_numerator = get_correlation_numerator(list_x, list_y)
    correlation_value = (correlation_numerator)/(math.sqrt(sum_of_correlation_squares(list_x)*sum_of_correlation_squares(list_y)))
    return correlation_value

# all stock pairs and their correlations from max to min:

print("My own implementation:")

import time
start_time = time.time()

print("MSFT:AMZN = " + str(get_correlation(allprices['MSFT'],allprices['AMZN'])))
print("AMZN:AAPL= " + str(get_correlation(allprices['AMZN'],allprices['AAPL'])))
print("MSFT:AAPL = " + str(get_correlation(allprices['MSFT'],allprices['AAPL'])))
print("GOOG:AMZN = " + str(get_correlation(allprices['GOOG'],allprices['AMZN'])))
print("IBM:FB = " + str(get_correlation(allprices['IBM'],allprices['FB'])))
print("GOOG:AAPL = " + str(get_correlation(allprices['GOOG'],allprices['AAPL'])))
print("GOOG:FB = " + str(get_correlation(allprices['GOOG'],allprices['FB'])))
print("MSFT:GOOG = " + str(get_correlation(allprices['MSFT'],allprices['GOOG'])))
print("IBM:GOOG = " + str(get_correlation(allprices['IBM'],allprices['GOOG'])))
print("FB:AMZN = " + str(get_correlation(allprices['FB'],allprices['AMZN'])))
print("IBM:AAPL = " + str(get_correlation(allprices['IBM'],allprices['AAPL'])))
print("FB:AAPL = " + str(get_correlation(allprices['FB'],allprices['AAPL'])))
print("IBM:AMZN = " + str(get_correlation(allprices['IBM'],allprices['AMZN'])))
print("MSFT:FB = " + str(get_correlation(allprices['MSFT'],allprices['FB'])))
print("IBM:MSFT = " + str(get_correlation(allprices['IBM'],allprices['MSFT'])))

part1 = "--- %s seconds ---" % (time.time() - start_time)
print(part1)
print("")

# MSFT:AMZN = 0.8741709140306773
# AMZN:AAPL= 0.8405047735028573
# MSFT:AAPL = 0.7910724697645043
# GOOG:AMZN = 0.6593918651991056
# IBM:FB = 0.6235315363005262
# GOOG:AAPL = 0.5831372907191038
# GOOG:FB = 0.5255643021735804
# MSFT:GOOG = 0.46331640746650576
# IBM:GOOG = 0.4224397164650116
# FB:AMZN = 0.04804592966462066
# IBM:AAPL = -0.024718866883184906
# FB:AAPL = -0.038716802228980905
# IBM:AMZN = -0.10170142015566165
# MSFT:FB = -0.29524958156416975
# IBM:MSFT = -0.4212553003530259
# --- 0.09494233131408691 seconds ---

# Part 2 - Write an one line numpy vectorized version of function correlation(x, y) 
# to compute the correlation of two lists x, and y.

import numpy as np

print("Numpy implementation:")

import time
start_time = time.time()

print("MSFT:AMZN = ")
print(str(np.corrcoef(allprices['MSFT'], allprices['AMZN'])))
print("")
print("AMZN:AAPL= ")
print(str(np.corrcoef(allprices['AMZN'], allprices['AAPL'])))
print("")
print("MSFT:AAPL = ")
print(str(np.corrcoef(allprices['MSFT'], allprices['AAPL'])))
print("")
print("GOOG:AMZN = ")
print(str(np.corrcoef(allprices['GOOG'], allprices['AMZN'])))
print("")
print("IBM:FB = ")
print(str(np.corrcoef(allprices['IBM'], allprices['FB'])))
print("")
print("GOOG:AAPL = ")
print(str(np.corrcoef(allprices['GOOG'], allprices['AAPL'])))
print("")
print("GOOG:FB = ")
print(str(np.corrcoef(allprices['GOOG'], allprices['FB'])))
print("")
print("MSFT:GOOG = ")
print(str(np.corrcoef(allprices['MSFT'], allprices['GOOG'])))
print("")
print("IBM:GOOG = ")
print(str(np.corrcoef(allprices['IBM'], allprices['GOOG'])))
print("")
print("FB:AMZN = ")
print(str(np.corrcoef(allprices['FB'], allprices['AMZN'])))
print("")
print("IBM:AAPL = ")
print(str(np.corrcoef(allprices['IBM'], allprices['AAPL'])))
print("")
print("FB:AAPL = ")
print(str(np.corrcoef(allprices['FB'], allprices['AAPL'])))
print("")
print("IBM:AMZN = ")
print(str(np.corrcoef(allprices['IBM'], allprices['AMZN'])))
print("")
print("MSFT:FB = ")
print(str(np.corrcoef(allprices['MSFT'], allprices['FB'])))
print("")
print("IBM:MSFT = ")
print(str(np.corrcoef(allprices['IBM'], allprices['MSFT'])))
print("")

part2 = "--- %s seconds ---" % (time.time() - start_time) 
print(part2)
print("")

# MSFT:AMZN = 
# [[ 1.          0.87417091]
# [ 0.87417091  1.        ]]

# AMZN:AAPL= 
# [[ 1.          0.84050477]
# [ 0.84050477  1.        ]]

# MSFT:AAPL = 
# [[ 1.          0.79107247]
# [ 0.79107247  1.        ]]

# GOOG:AMZN = 
# [[ 1.          0.65939187]
# [ 0.65939187  1.        ]]

# IBM:FB = 
# [[ 1.          0.62353154]
# [ 0.62353154  1.        ]]

# GOOG:AAPL = 
# [[ 1.          0.58313729]
# [ 0.58313729  1.        ]]

# GOOG:FB = 
# [[ 1.         0.5255643]
# [ 0.5255643  1.       ]]

# MSFT:GOOG = 
# [[ 1.          0.46331641]
# [ 0.46331641  1.        ]]

# IBM:GOOG = 
# [[ 1.          0.42243972]
# [ 0.42243972  1.        ]]

# FB:AMZN = 
# [[ 1.          0.04804593]
# [ 0.04804593  1.        ]]

# IBM:AAPL = 
# [[ 1.         -0.02471887]
# [-0.02471887  1.        ]]

# FB:AAPL = 
# [[ 1.        -0.0387168]
# [-0.0387168  1.       ]]

# IBM:AMZN = 
# [[ 1.         -0.10170142]
# [-0.10170142  1.        ]]

# MSFT:FB = 
# [[ 1.         -0.29524958]
# [-0.29524958  1.        ]]

# IBM:MSFT = 
# [[ 1.        -0.4212553]
# [-0.4212553  1.       ]]

# --- 0.0552830696105957 seconds ---

# Part 3: Compare the run time of both implementations.
print("Run time of Part 1 implementation: " + str(part1))
print("Run time of Part 2 implementation: " + str(part2))
print("")
print("Run time of Part 1 implementation is longer than the run time of Part 2 implementation.")
print("This shows us that using numpy is better suited for calculating the correlation coefficient.")
print("This is likely because Numpy functions are implemented in C, and also may have better implementation. https://towardsdatascience.com/how-fast-numpy-really-is-e9111df44347#:~:text=Because%20the%20Numpy%20array%20is,leap%20in%20terms%20of%20speed.")

# Run time of Part 1 implementation: --- 0.06476306915283203 seconds ---
# Run time of Part 2 implementation: --- 0.0552830696105957 seconds ---

# Run time of Part 1 implementation is longer than the run time of Part 2 implementation.
# This shows us that using numpy is better suited for calculating the correlation coefficient.
# This is likely because Numpy functions are implemented in C, and also may have better implementation. https://towardsdatascience.com/how-fast-numpy-really-is-e9111df44347#:~:text=Because%20the%20Numpy%20array%20is,leap%20in%20terms%20of%20speed.

