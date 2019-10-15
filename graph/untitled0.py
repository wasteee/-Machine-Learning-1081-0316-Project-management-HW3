# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:06:01 2019

@author: fghj8
"""

import random
import matplotlib as mpl
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['font.size'] = 10
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for z in range(5):
    xs = range(1,13)
    ys = 10 * np.random.rand(12)
    color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
    ax.bar(xs, ys, zs=z, zdir='y', color=color, alpha=0.8)

ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))
ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('data')
plt.show()

