# -*- coding: utf-8 -*-
"""
Created on Sun Agst  6 12:33:38 2023

@author: Hamza Dilbaz
"""
#Histogram Denkleştirme
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/Users/bilal/Desktop/blender.jpg',0)
hist,bins= np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf*float(hist.map()) / cdf.max()
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc='upper left')
plt.show()

