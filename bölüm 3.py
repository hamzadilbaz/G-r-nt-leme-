# -*- coding: utf-8 -*-
"""
Created on Sun Agst  6 11:25:20 2023

@author: Hamza Dilbaz
"""
#İkili görüntü
import cv2
import numpy as np
height = 512
width = 512

img = np. random.randint(255, size = (height,width,1), dtype=np.uint8)
cv2.imshow( ' Binary ' , img)

#matris indeksleme

import numpy as np

a = np.array([[1,4,5],
             [-5,8,9],
             [6,8,10],
             [0,2,38]])

print("type:" , type(a))
print("a = ","\n",a,"\n")
print("a[1] = ",a[1])
print("a[1][2] =", a[1][2])
print("a[0][-1] =",a[0][-1])

#Görüntüleri Okuma Yazma
import cv2
import numpy as np
import matplotlib.pyplot as plt


resim1= cv2.imread("/Users/bilal/Desktop/blender.jpg")

cv2.imshow("Brain",resim1)
print(resim1.size)
print(resim1.dtype)
print(resim1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Yoğunluk resmi
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
row = 256
col = 256
img = np.zeros((row,col))
img[100:105, :] = 0.5
img[:,100:105] = 1
plt.figure(figsize=(10,4))
plt.imshow(img)
plt.show
