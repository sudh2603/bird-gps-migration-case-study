# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 12:02:56 2018

@author: sudhanshu kumar sinh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bird_tracking=pd.read_csv("bird_tracking.csv")

plt.figure(figsize=(7,7))
bird_names=pd.unique(bird_tracking.bird_name)   #filter unique entity from the series
for i in bird_names:
    ix = bird_tracking.bird_name== i  #form a panda-series consisting boolen entity
    x , y = bird_tracking.longitude[ix],bird_tracking.latitude[ix]    #x,y become a panda series cosisting entity value of longitude and latitude respectively
    plt.plot(x,y,".",label=i)
    
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("bird_trajactory.pdf")

