#Smoothing and blurring of the images too kill noise
import numpy as np

import cv2

cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	#Huge saturation value
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_blue=np.array([150,150,50])
	upper_blue=np.array([180,255,255])



	mask=cv2.inRange(hsv,lower_blue,upper_blue)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	#Applying simple kernel
	kernel = np.ones((15,15),np.float32)/225
	smoothed=cv2.filter2D(res,-1,kernel)
	#Guassian Blur
	blur=cv2.GuassianBlur(res,(15,15),0)
	#Median Blur
	median=cv2.medianBlur(res,15)
	#bilateral
	bilateral=cv2.bilateralFilter(res,15,27,75)

	cv2.imshow('frame',frame)
	cv2.imshow('smoother',smoothed)
	cv2.imshow('res',res)
	cv2.imshow('Blue',Blur)
	cv2.imshow('Median Blur',median)
	cv2.imshow('Bilateral',bilateral)
	

	k=cv2.waitKey(5) & 0xFF
	if k == 27:
		break


cv2.destroyAllWindows()
cap.release()