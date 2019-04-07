import numpy as np
import gzip
import datetime
import os
import os.path
import pandas as pd

# date0 = datetime.datetime.strptime('20010101','%Y%m%d')
with open('station.txt') as a:
    station_list = list(a)

# read op file seperately
def line2desc(data):
    stn = data[:6]
    wban = data[7:12]
    date = data[13:23]
    temp = float(data[24:30])
    if temp == 9999.9:
        temp = np.nan
        
    dewp = float(data[35:41])
    if dewp == 9999.9:
        dewp = np.nan

    slp = float(data[46:52])
    if slp == 9999.9:
        slp = np.nan

    stp = float(data[57:63])
    if stp == 9999.9:
        stp = np.nan

    MAX = float(data[102:108])
    if MAX == 9999.9:
        MAX = np.nan

    MIN = float(data[110:116])
    if MIN == 9999.9:
        MIN = np.nan

    prcp = float(data[118:123])
    if prcp == 99.99:
        prcp = np.nan

    return [stn + '-' + wban, date, temp, dewp, slp, stp, MAX, MIN, prcp]

# read_gz_op
def read_op(name):
    infile = gzip.GzipFile(name,'r')
    lines = infile.readlines()
    test = []
    for i in range(1,len(lines)):
        test.append(lines[i].decode('utf-8'))
    return(test)

year = ["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
col = ['STN-WBAN', 'DATE', 'TEMP', 'DEWP', 'SLP', 'STP', 'MAX', 'MIN', 'PRCP']
for j in range(len(station_list)):
    total = []
    csv_name = os.path.join(".","GSOD-final",station_list[j][0:6]+'-'+station_list[j][6:11]+'.csv')
    for i in range(len(year)):
        yy = year[i]
        temp_name = station_list[j][0:6]+'-'+station_list[j][6:11]+'-'+yy+'.op.gz'
        file_name = os.path.join(".","GSOD-useful-station","gsod_"+yy,temp_name)
        op_temp = read_op(file_name)
        for l in range(len(op_temp)):
            ll = line2desc(op_temp[l])
            total.append(ll)
    
    tt = pd.DataFrame(columns=col,data=total)
    tt.to_csv(csv_name,encoding='gbk')
