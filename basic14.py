#Feature matching

import cv2
import numpy as np
import matplotlib.pyplot as plt

#matplotlitb-->RGB while CV displays BGR

img1=cv2.imread('template.jpg',1)
img2=cv2.imread('big.jpg',1)

#detector

orb=cv2.ORB_create()

#key points and descriptors
kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches = bf.match(des1,des2)
matces = sorted(matches,key=lambda x:x.distance)

img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:100],None,flags=2)
plt.imshow(img3)
plt.show()