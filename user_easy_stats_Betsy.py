"""

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

# Descriptive: Univariant Data..................................

# univariant data (one variable, many readings)
uni_data = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]
logger.info("uni_data = " + str(uni_data))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)



# Descriptive: Univariant Time Series Data.........................

# describe relationships
# univariant time series data (one variable over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

# if the lists are not the same size,
# log an error and quit the program
if len(xtimes) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xtimes)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the new correlation function from the statistics module
xx_corr = statistics.correlation(xtimes, xtimes)
xy_corr = statistics.correlation(xtimes, yvalues)

# log the information
logger.info("Here's some time series data:")
logger.info(f"xtimes:{xtimes}")
logger.info(f"yvalues:{yvalues}")
logger.info(f"correlation between xtimes and xtimes = {xx_corr:.2f}")
logger.info(f"correlation between xtimes and yvalues = {xy_corr:.2f}")

# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)

arrayX = [-200, -150, -100, 50, 0, 50, 100, 150]
arrayY = [-240, -165, -99, 35, 19, 75, 130, 125]

#Find the Mean,Median,Mode, and Range of the 2 data sets

import statistics
data_a = [200, 150, 100, 50, 0, 50, 100, 150]
data_b = [-240, -165, -99, 35, 19, 75, 130, 125]

mean_data_a = statistics.mean(data_a)
median_data_a = statistics.median(data_a)
mode_data_a = statistics.mode(data_a)
variance_data_a = statistics.variance(data_a)


mean_data_b = statistics.mean(data_b)
median_data_b = statistics.median(data_b)
mode_data_b = statistics.mode(data_b)
variance_data_b = statistics.variance(data_b)

print("Mean of data a:", mean_data_a)
print("Mean of data b:", mean_data_b)
print("Median of data a:", median_data_a)
print("Median of data b", median_data_b)
print("Mode of data 1:", mode_data_a)
print("Mode of data b:", mode_data_b)
print("Variance of data a:", variance_data_a)
print("Variance of data b:", variance_data_b)
print("Standard Deviation of data a:", statistics.stdev(data_a))
print("Standard Deviation of data b:", statistics.stdev(data_b))
print("Smallest number in data a:", min(data_a))
print("Smallest number in data b:", min(data_b))
print("Largest number in data a:", max(data_a))
print("Largest number in data b:", max(data_b))
print("Range of data a:", max(data_a)- min(data_a))

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayX, arrayY)

# Choose an x value off in the future (future x)
future_x = 200

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{arrayX}")
logger.info(f"y:{arrayY}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")