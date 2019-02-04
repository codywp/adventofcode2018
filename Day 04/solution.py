import numpy as np
import pandas as pd

df = pd.read_csv("input.csv")
df['Time'] = pd.to_datetime(df['Time'], format= '%H:%M' ).dt.time
s_df = df.sort_values(['Date','Time'])

schedule = {}
pid = -1

for ind, row in s_df.iterrows():
        date = row['Date']
        minute = row['Time'].minute
        if row['Action'][0] == '#':
                pid = int(row['Action'][1:])
                if pid not in schedule:
                        schedule[pid] = [0 for i in range(0,60)]
                #if row['Time'].hour > 0:
                #        date = "{0}{1}".format(date[:-1], (int(date[-1]) + 1))
                #        break
        else:
                schedule[pid][minute:]  = [i + int(row['Action']) for i in schedule[pid][minute:]]
maxid = -1
sleepHr = -1
maxVal = -1
for k,v in schedule.items():
        if sum(v) > maxVal: #np.max(v)
                maxVal=sum(v)
                sleepHr=np.argmax(v)
                maxid = k

print maxid*sleepHr
