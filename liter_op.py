import pandas as pd
import numpy as np
import os.path
from numpy import *
from datetime import datetime

# 时间序列
time = pd.date_range('20010101','20181231')
col = ['STN-WBAN', 'DATE', 'TEMP', 'DEWP', 'SLP', 'STP', 'MAX', 'MIN', 'PRCP']
with open('station.txt') as a:
    station_list = list(a)

cor_frame = pd.DataFrame(pd.read_csv('time.csv'))
# return value
def return_value(stn,line,frame):
    ddate = frame['DATE'][line]
    TEMP = float(frame['TEMP'][line])
    DEWP = float(frame['DEWP'][line])
    SLP = float(frame['SLP'][line])
    STP = float(frame['STP'][line])
    MAX = float(frame['MAX'][line])
    MIN = float(frame['MIN'][line])
    PRCP = float(frame['PRCP'][line])
    return [stn, ddate, TEMP, DEWP, SLP, STP, MAX, MIN, PRCP]
# comparison 
def com_data(station_name,csv_name):
    station_frame = pd.DataFrame(pd.read_csv(station_name))
    stn = station_frame['STN-WBAN'][1]
    total = []
    row = 0
    for i in range(len(time)):
        if i-row <= len(station_frame['DATE'])-1:
            if cor_frame['DATE'][i] == station_frame['DATE'][i-row]:
                ll = return_value(stn,i-row,station_frame)
                total.append(ll)
            else:
                ll = return_value(stn,i,cor_frame)
                total.append(ll)
                row = row + 1
    tt = pd.DataFrame(columns=col,data=total)
    tt.to_csv(csv_name,encoding='gbk')

for i in range(len(station_list)):
    temp_name = station_list[i][0:6]+'-'+station_list[i][6:11]+'.csv'
    file_name = os.path.join(".","GSOD-final",temp_name)
    csv_name = os.path.join(".","GSOD-final-cor",temp_name)
    print(temp_name)
    com_data(file_name,csv_name)




