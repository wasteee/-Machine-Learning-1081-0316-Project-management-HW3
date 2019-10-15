# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:09:26 2019

@author: fghj8
"""
import pickle
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt


dirpath = 'C:\\Users\\fghj8\\MLGame-master\\games\\arkanoid\\Log\\kmeans'
BallPosition = []
PlatformPosition = []
LRUP = []
Slope = []
last_ball_x = 0
last_ball_y = 0
files = listdir(dirpath)
log_number = 0
Frame = []
for k in range(0,1):
    for f in files:
      log_number = log_number + 1
      fullpath = join(dirpath, f)
      if isfile(fullpath):
        with open(fullpath , "rb") as f1:
            data_list1 = pickle.load(f1)
        for i in range(0 , len(data_list1)):
            BallPosition.append(data_list1[i].ball)
            PlatformPosition.append(data_list1[i].platform)
            
            if(last_ball_x - data_list1[i].ball[0] > 0):
                LR = 1
            else:
                LR = 0
            if(last_ball_y - data_list1[i].ball[1] > 0):
                UP = 0
            else:
                UP = 1
            LRUP.append(np.array((LR,UP)))
            delta_x = int(data_list1[i].ball[0]) - int(last_ball_x)
            delta_y = int(data_list1[i].ball[1]) - int(last_ball_y)
            #get Slope
            #print(fullpath)
            try:
                m = delta_y/delta_x
            except:
                print(fullpath)
            Slope.append(np.array((m,data_list1[i].platform[0])))
            
            last_ball_x = data_list1[i].ball[0]
            last_ball_y = data_list1[i].ball[1]


PlatX = np.array(PlatformPosition) [:,0][:,np.newaxis]
PlatX_next = PlatX[1:,:]
instrust = (PlatX_next-PlatX[0:len(PlatX_next),0][:,np.newaxis])/5 +1 

Ballarray = np.array(BallPosition[:-1])
LRUP = np.array((LRUP[:-1]))
S = np.array((Slope[:-1]))
x = np.hstack((Ballarray,LRUP,S))

plt.plot(BallPosition[0],BallPosition[1])
plt.xlabel('x')
plt.ylabel('y')
plt.show
