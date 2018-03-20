#image arithametic and logical Operations

import cv2
import numpy as np 

img1=cv2.imread('C1.png')
img2=cv2.imread('C4.png')




#operations
add = img1 + img2
add2=cv2.add(img1,img2)
weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)

#tresholding the image
rows,cols,channels=img2.shape
roi=img2[0,rows,0:cols]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('mask',mask)


mask_inv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
dst=cv2.add(img1_bg,img1_fg)

img1[0:rows,0:cols]=dst
cv2.imshow('RES',img1)




#displaying
cv2.imshow('add',add)
cv2.imshow('add2',add2)
cv2.imshow('add with weights',weighted)


#closing
cv2.waitKey(0)
cv2.destroyAllWindows()

