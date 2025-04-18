import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import datetime
from pandas.tseries.holiday import USFederalHolidayCalendar

counts= pd.read_csv('python_first/FremontBridge.csv',index_col='Date', parse_dates=True)
weather =pd.read_csv('python_first/BicycleWeather.csv',index_col='DATE',parse_dates=True)
print(counts.head(3))
weather.info()
print(weather.head(3))
daily= counts.resample('d').sum()
daily['Total'] =daily.sum(axis=1)
daily = daily[['Total']]

print(daily.head(3))
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for i in range(len(days)):
    daily[days[i]]=(daily.index.dayofweek ==i).astype(float) #astype은 데이터 타입을 변환하는 메소드
# for i in dir(daily.index):
#     print(i)
print(daily.head(7))
cal = USFederalHolidayCalendar()
holidays = cal.holidays('2012','2016')
daily= daily.join(pd.Series(1, index= holidays, name='holiday'))
# print("2012 holiday",daily.loc['2012'].sample(5))
daily['holiday'].fillna(0, inplace=True)
print(daily.head(3))
# 일조시간에 자전거를 타는 사람
def hours_of_daylight(date, axis=23.44, latitude=47.61):
 # 해당 날짜의 일조시간 계산
 days = (date - pd.to_datetime('2000, 12, 21')).days
 m = (1. -np.tan(np.radians(latitude))
 * np.tan(np.radians(axis) * np.cos(days * 2 * np.pi / 365.25)))
 return 24 * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180.
daily['daylight_hrs'] = list(map(hours_of_daylight, daily.index))
daily[['daylight_hrs']].plot()
plt.ylim(8, 17)
# plt.show()
weather['TMIN'] /= 10
weather['TMAX'] /= 10
weather['Temp(F)'] = 0.5 * (weather['TMIN'] + weather['TMAX'])
weather['PRCP'] /= 254 # weather['PRCP'] = weather['PRCP'] /254
weather['dry day'] = (weather['PRCP']== 0).astype(int)
daily =daily.join(weather[['PRCP','Temp(F)','dry day']])
print(daily.head(10))
daily['annual']= (daily.index - daily.index[0]).days /365.
print(daily.sample())
daily.dropna(axis=0,how='any',inplace=True)
column_names = ['Mon','Tue','Wed',"Thu","Fri",'Sat',"Sun","holiday",'daylight_hrs','PRCP',"dry day",'Temp(F)','annual']
X= daily[column_names]
y=daily['Total']
print(X.head(3))
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False) #인공지능 학생
model.fit(X,y) #학습시키다
daily['predicted'] = model.predict(X) # 검증, 모의고사, 테스트...(맞춰봐)
daily[['Total','predicted']].plot(alpha=0.5)
params= pd.Series(model.coef_,index=X.columns)
print("params:",params)
plt.show() 
from sklearn.utils import resample
np.random.seed(1)
err = np.std([model.fit(*resample(X,y)).coef_ for i in range(1000)],0)
print(pd.DataFrame({'effect': params.round(0), 'error':err.round(0)}))