import pandas as pd

#since the kernel saves the files in a log as pandas dataframe, hence we use this technique.
df = pd.read_pickle('EXCHANGE_AGENT.bz2')

#len(df)

df = df.drop(df.index[0])

df.to_csv('exchange.csv')

df = pd.read_csv('exchange.csv')#this is the csv file to be used in ProM


#configuring cases
from datetime import datetime

df = df.sort_values('EventTime', ascending=True).reset_index(drop=True)
date_to_minute = df['EvetnTime'].map(lambda d: datetime.strptime(d[:-3],'%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M'))
previous_date_time = date_to_minute[0]
#if you want case column to start from 1, change this variable to 1
current_case = 0
cases = []
for current_date_time in date_to_minute:
    if current_date_time > previous_date_time:
        current_case += 1
    cases.append(current_case)
    previous_date_time = current_date_time #missed adding this line previously
df['cases'] = pd.Series(cases, name='cases')
