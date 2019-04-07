import numpy as np
import os
import os.path
import gzip
import shutil
year = ["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]

with open('station.txt') as a:
    station_list = list(a)

for i in range(len(year)):
    yy = year[i]
    for j in range(len(station_list)):
        temp_name = station_list[j][0:6]+'-'+station_list[j][6:11]+'-'+yy+'.op.gz'
        infile = os.path.join(".","GSOD","gsod_"+yy,temp_name)
        outfile = os.path.join(".","GSOD-useful-station","gsod_"+yy,temp_name)
        shutil.copy(infile,outfile)
        