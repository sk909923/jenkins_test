import requests
import pandas as pd
response = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json")
d = response.json()
new_df=pd.DataFrame(d['AFG'])
new_df1=new_df.loc[:,['continent','location','population','population_density','aged_65_older','aged_70_older','cardiovasc_death_rate']]
#print(new_df)
df = pd.DataFrame(d['AFG']["data"])
#print (df.tail())
mydata=df.loc[:,'date':'new_deaths']
#print(mydata)
death=df.iloc[:,1:5]
#print(death)
newdata=df.loc[:,['date','total_cases','total_deaths']]
#print(newdata)
alldata=pd.concat([new_df, df], axis=1)



#df['month'] = pd.DatetimeIndex(df['date']).month
#print(df['month'])
df['yyyy-mm'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m')
#print(df['yyyy-mm'])
df_date=df['yyyy-mm'].str[2:]
#print(df_date)
new_cases=df.loc[:, ['new_cases']]
#print(new_cases)
total_cases=mydata.loc[:,['total_cases']]
#print(total_cases)
total_deaths =mydata.loc[:,['total_deaths']]
new_deaths =mydata.loc[:,['new_deaths']]

alldata.to_csv('covid_data.csv', index=False)
from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
df = AV.AutoViz("covid_data.csv")




