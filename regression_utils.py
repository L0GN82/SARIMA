import math
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
""" This module will house utility functions that need to be created for 
simplifying views of data models and results. It is assumed that all parameters passed
will either be numpy arrays, pandas Series, or pandas DataFrames. """


def regressionSummary(y_actual, y_predicted, x_df):
    """ Returns regression characteristics from comparison of
    actual (historical) values to estimated (predicted) ones. """

    y_actual = np.asarray(y_actual)
    y_predicted = np.asarray(y_predicted)
    y_residual = y_actual - y_predicted

    metrics = [
        ('Mean Error (ME): ', sum(y_residual) / len(y_residual)),
        ('Root Mean Squared Error (RMSE): ', math.sqrt(mean_squared_error(
                                                       y_actual,y_predicted))),
        ('Mean Absolute Error (MAE): ', sum(abs(y_residual)) / len(y_residual)),
        ('Mean Percent Error (MPE): ', 100 * sum(y_residual / y_actual) / len(y_residual)),
        ('Mean Absolute Percent Error (MAPE): ', 100 * sum(abs(y_residual / y_actual) / len(y_residual))),
        ('R squared : ', R_squared(y_actual, y_predicted)),
        ('Adjusted R squared: ', adj_R_squared(y_actual, y_predicted, x_df))
    ]

    for metric in metrics:
        print(metric)
    print("\n\n")

def R_squared(y_actual, y_predicted):
    """ Calculates R squared, which is equivalent to 1 - (sum of squared residuals/sum of squared total).
    y_actual and y_predicted are numpy arrays, or pandas series, or a dataframe slice.

    A residual is equal to the actual value minus the predicted value.
    An error, for sum of square errors, is equal to the actual value minus the average """

    # residual is (y_actual - y_predicted), ss_residual is the squared residual
    ss_residual = np.sum((y_actual - y_predicted) ** 2)

    # error is (y_actual - np.mean(y_actual)), ss_total is the squared error
    ss_total = np.sum((y_actual - np.mean(y_actual)) ** 2)

    r_square = 1 - (ss_residual / ss_total)
    return r_square


def adj_R_squared(y_actual, y_predicted, x_df):
    """ Calculates the adjusted R squared value using the R_squared function.
     Adjusted R squared is equal to 1 - ( (sum of squared residuals/degrees freedom residual) / (sum of squared total/degrees freedom total) )
     where degrees freedom of the residual = n - p (#vars) - 1 and degrees freedom total = n - 1

     This gives us adj_R_squared = 1 - ( ((1 - R^2) * (n - 1)) / n - p - 1) where n = num observations and
                                                                                  p = num variables """

    r_squared = R_squared(y_actual, y_predicted)
    
    n = len(y_actual)
    p = x_df.shape[1]
    
    if n <= p + 1:
        raise ValueError("Not enough observations for the number of predictors.")
    
    adj_r = 1 - ((1 - r_squared) * (n - 1) / (n - p - 1))
    
    return adj_r


