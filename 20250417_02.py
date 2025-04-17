import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
data = pd.read_csv("C:/Users/hi/Desktop/job/python/python_first/FremontBridge.csv",index_col="Date",parse_dates=True)
print(data.head(5))
cols =['East',"West"]
data.columns = cols
data['Total']=data.eval('East+West')# data['Total']= data['East']+data['West']
print(data.head(5))
print(data.describe())
data.info()
# seaborn.set()
data.plot()
# plt.ylabel('Hourly Bicycle Count')
# plt.show()

weekly = data.resample('W').sum()
weekly.plot(style=[':','--','-']) 
plt.ylabel('Weekly bicycle count')
plt.show()
