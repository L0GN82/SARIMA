#This script is designed to read the RRC data and clean it.
import pandas as pd
import matplotlib.pyplot as plt
#RRC oil barrel production
df = pd.read_csv(r'C:\Users\LoganFrideley\OneDrive - East Texas Salt Water Disposal Company\Documents\SARIMA Project\ProductionDataQuery_monthlyTotals_ReportCSV(1).csv')

oil_prod = df[['Date', 'Barrels']]

#FRED Brent-Crude oil pride index
df2 = pd.read_csv(r'C:\Users\LoganFrideley\OneDrive - East Texas Salt Water Disposal Company\Documents\SARIMA Project\MCOILBRENTEU.csv')

oil_price = df2[['Date', 'Price']]




#Figure for the oil_prod dataframe
fig, ax = plt.subplots(figsize=(15,8), layout = 'constrained')
ax.plot(oil_prod['Date'], oil_prod['Barrels'])
ax.set_xlabel('Date')
ax.set_ylabel('Oil Production')
ax.set_title('East Texas Oil Field Production')


#figure for the oil_price dataframe
fig, ax = plt.subplots(figsize=(15,8), layout = 'constrained')
ax.plot(oil_price['Date'], oil_price['Price'])
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Crude Oil Prices')
fig.autofmt_xdate()


#plt.show()