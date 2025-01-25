import statistics 
import numpy as np
stock_prices = [100,102,98,105,101,97,99,103,100,98]

variance = statistics.variance(stock_prices)
print(f"Variance of stock prices: {variance}")

numpy_variance = np.var(stock_prices,ddof=1)
print(f"Variance of stock prices (using NumPy): {numpy_variance}")
'''import pandas as pd
import seaborn as sns 
import matplotib.pyplot as plt 

data = {
    'Temperature': [1,2,3],
    "humidity":[3,4,5],
    'Wind speed':[4,5,6],
    'pressure':[6,7,8]
}
df.pd.DataFrame(data)
plt.figure(figsize=(8,6))
plt.scatter(df['Temperature'],df['humidity'],color='blue',label='Temp vs humidity')
plt.title("Temperature vs humidy",fontsize=14)'''
