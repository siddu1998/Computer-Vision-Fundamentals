#Background extraction
#Basic algorithm is compare current and previous frame and plot changes accordinglt
import cv2
import numpy as np


cap = cv2.VideoCapture(0)

#fore-ground
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret,frame=cap.read()
	fgmask=fgbg.apply(frame)
	#cv2.imshow('original',frame)
	cv2.imshow('mask',fgmask)

	k=cv2.waitKey(5) & 0xFF
	if k == 27:
		break


cv2.destroyAllWindows()
cap.release()