# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 23:58:33 2018

@author: sudhanshu kumar sinh
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

birddata=pd.read_csv("bird_tracking.csv")

# First, use `groupby()` to group the data by "bird_name".
grouped_birds =birddata.groupby(birddata.bird_name)

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = np.mean(birddata.speed_2d)

# Use the `head()` method prints the first 5 lines of each bird.
grouped_birds.head()

# Find the mean `altitude` for each bird.
mean_altitudes = []

for name,group in grouped_birds:
    mean_altitudes.append(np.mean(group.altitude))

birddata.date_time = pd.to_datetime(birddata.date_time)

# Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date

# Check the head of the column.
birddata.date.head()

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby("date")

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates.altitude.mean()

# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby([birddata.bird_name,birddata.date])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday =grouped_birdday.altitude.mean()

# look at the head of `mean_altitudes_perday`.
mean_altitudes_perday.head()

avg_speed=grouped_birdday.speed_2d.mean()
eric_daily_speed  = birddata[birddata.bird_name=="Eric"].groupby("date").speed_2d.mean()
sanne_daily_speed = birddata[birddata.bird_name=="Sanne"].groupby("date").speed_2d.mean()
nico_daily_speed  = birddata[birddata.bird_name=="Nico"].groupby("date").speed_2d.mean()

plt.figure(figsize=(10,10))
eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.savefig("Birds Altitude.pdf")