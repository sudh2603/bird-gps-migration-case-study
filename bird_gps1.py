# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:16:32 2018

@author: sudhanshu kumar sinh
"""

from bird_gps import bird_tracking,bird_names
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature


plt.figure(figsize=(8,4))
speed=bird_tracking.speed_2d[bird_tracking.bird_name=="Eric"]
ind= np.isnan(speed)
plt.hist(speed[~ind],bins=np.linspace(0,20,30),normed=True)
plt.xlabel("2D Speed (m/sec)")
plt.ylabel("Frequency")
#plt.savefig("hist.pdf")
def panda_plot(bird_tracking):
    bird_tracking.speed_2d.plot(kind="hist",range=[0,30])
    plt.xlabel("2D Speed (m/sec)")
    plt.ylabel("Frequency")



plt.figure(figsize=(8,5))   
time_stamp=[]
for k in range(len(bird_tracking)):
    time_stamp.append(datetime.datetime.strptime(bird_tracking.date_time.iloc[k][:-3],"%Y-%m-%d %H:%M:%S"))   #convert the time in string format to datetime-timestamp and append it
    
bird_tracking["timestamp"]=pd.Series(time_stamp , index=bird_tracking.index)
times=bird_tracking.timestamp[bird_tracking.bird_name == "Eric"]
elapsed_time=[i_time-times[0] for i_time in times]
plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed Time (Days)")
plt.savefig("timeplot.pdf")



data=bird_tracking[bird_tracking.bird_name == "Eric"]
times_data=data.timestamp
elapsed_time_data= [time_k-times_data[0] for time_k in times_data]

next_day=1
inds=[]
daily_mean_speed=[]
for (i,j) in enumerate(elapsed_time_data):
    if j/datetime.timedelta(days=1) < next_day:
        inds.append(i)
        
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))    #calculate mean speed of a day and append
        next_day+= 1
        inds=[]
        
plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/sec)")
plt.savefig("Mean_speed_plot.pdf")

proj=ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection= proj)
ax.set_extent((-25.0,20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

for name in bird_names:
    ix=bird_tracking.bird_name == name   #return a panda-series consisting boolean value on the basis of desire bird name
    x,y = bird_tracking.longitude[ix], bird_tracking.latitude[ix]
    ax.plot(x,y, '.',transform=ccrs.Geodetic(), label=name)
    
plt.legend(loc= "upper left")
plt.savefig("map.pdf")

