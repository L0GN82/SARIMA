import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

#The goal of this script is to access the excel data and isolate the columns for the SARIMA model.
#Included is a stationarity function
#Training an Validation data are also created (This is unadjusted data!!!)


df = pd.read_excel(r"C:\Users\LoganFrideley\East Texas Salt Water Disposal Company\Finance - Documents\Water Disposal History.xlsx")
#pd.set_option('display.max_rows', 90)

monthly_water_vols = df[['Month/ Year', 'Total Disposed Water Volume']].copy()
# Filter out all Na values for water volumes.
monthly_water_vols = monthly_water_vols[~monthly_water_vols['Total Disposed Water Volume'].isna()]
# Changing column names to 'Water Volume'
monthly_water_vols['Water Volume'] = monthly_water_vols['Total Disposed Water Volume']
# Changing column name to Date and also making the type datetime64
monthly_water_vols['Date'] = monthly_water_vols['Month/ Year']
monthly_water_vols['Date'] = pd.to_datetime(monthly_water_vols['Date'])

# change Date to a Period data type
monthly_water_vols['Date'] = monthly_water_vols['Date'].dt.to_period(freq='M')

# Dropping the old columns
monthly_water_vols = monthly_water_vols.drop(columns = ['Total Disposed Water Volume', 'Month/ Year'])
# Changing the order of the columns
monthly_water_vols = monthly_water_vols.loc[:, ['Date', 'Water Volume']]
# This function checks if the data has 'stationarity'
#Also checks and prints the p_value
# Uses the augmented Dickey-Fuller test


def check_stationarity(timeseries):
    result = adfuller(timeseries, autolag = 'AIC')
    p_value = result[1]
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {p_value}')
    print('Stationary' if p_value < 0.05 else 'Non-stationary')


check_stationarity(monthly_water_vols['Water Volume'])

#Changing the dataframe to represent the last 5 years.
mask = (monthly_water_vols['Date'] >= '2021-01') & (monthly_water_vols['Date'] <= '2026-07')
subset = monthly_water_vols[mask]

#Assigning Training data set
training_mask = (subset['Date'] >= '2021-01') & (subset['Date'] <= '2026-02')
training = subset[training_mask]

#Assigning Validation data
validation_mask = (subset['Date'] >= '2026-03') & (subset['Date'] <= '2026-07')
validation = subset[validation_mask]

training_data = np.asarray(training['Water Volume'])





