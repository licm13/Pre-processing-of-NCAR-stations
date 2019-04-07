# Step 1. 手动解压每一年的tar
# Step 2. 读取tar里面的gz列表，筛出每年可用的站点编号，存成一行
# Step 3. 集合所有年份，成一个大的表
# Step 4. 做并集操作，导出excel

import gzip
import os
import numpy as np

# 函数用于筛选出有效天数>90的站点序列号
def useful_station_list(inpath,year,useful_station_id):    
    filelist = os.listdir(inpath)
    useful_station = []
    for i in range(1,len(filelist)):
        inname = os.path.join(inpath,filelist[i])
        infile = gzip.GzipFile(inname,'r')
        lines = infile.readlines()
        if len(lines) > 330:
            useful_station.append(filelist[i][0:6]+filelist[i][7:12])
        
    # save to txt
    out_filename = 'useful_station'+'_'+year+'.txt'
    file_save = open(out_filename,'w')
    for i in useful_station:
        file_save.write(i)
        file_save.write('\n')
    file_save.close()

year = ["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
useful_station_id = np.ones((6,18),dtype=np.str)
for i in range(len(year)):
    inpath = os.path.join(".","GSOD",'gsod_'+year[i])
    useful_station_list(inpath,year[i],useful_station_id)
    print(year[i])