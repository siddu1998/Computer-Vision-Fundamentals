#Tresholding using opencv

import cv2
import numpy as numpy

img=cv2.imread('bookpage.jpg')

#Normal Threshold
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)



#Gaussian Threshold
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

#Display
cv2.imshow('Original',img)
cv2.imshow('threshold',threshold)

cv2.imshow('Gray Scale',grayscaled)
cv2.imshow('Gray threshold',threshold2)
cv2.imshow('Gaus',gaus)

#to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()


