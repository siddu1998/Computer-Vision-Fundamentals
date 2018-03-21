import cv2
import numpy as np

img_rgb = cv2.imread('IMAGE WHERE YOU WANT TO FIND THE ELEMENT')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('WHAT IMAGE YOU WANT TO FIND',0)
#Shape of template that we need to search...we use this to draw bonxe
w, h = template.shape[::-1]
#to compute the result that is possibility of the template being matached
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#if thte template matched confidence is greater than 0.8 (this is a custom value)
threshold = 0.8
#then add it a array
loc = np.where( res >= threshold)
#draw rectangle around it.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)