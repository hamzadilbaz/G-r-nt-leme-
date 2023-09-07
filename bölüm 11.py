# -*- coding: utf-8 -*-
"""
Created on Sun Agst  6 10:38:31 2023

@author: Hamza Dilbaz
"""
## Bölüm 11


## Thresholding Kod Örneği

import cv2
import numpy as np
image =cv2.imread('/Users/bilal/Desktop/blender.jpg',0)

ret1 , thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

ret2,thresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("orjinal resim",image)
cv2.imshow("simple thresholding",thresh1)
cv2.imshow("otsu thresholding", thresh2)
cv2.imwrite("Simple Thresholding.jpg", thresh1)
cv2.imwrite("Otsu Thresholding.jpg", thresh2)
cv2.imwrite("Orginal Image.jpg", image)

##Canny Kenar Tespiti Örnek



image = cv2.imread("/Users/bilal/Desktop/blender.jpg")

#Resmi griye dönüştürme
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#görüntüyü blurlama
blur = cv2.GaussianBlur(gray, (5,5), 0)

canny = cv2.Canny(blur,75,225)

cv2.imshow("blurred image",blur)
cv2.imshow("canny image",canny)
cv2.imwrite("output canny.jpg", canny)
cv2.imwrite("Blur Output.jpg", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()


