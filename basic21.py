import cv2
import numpy as np 


img=cv2.imread('redcap.jpg',0)
ret,thresh=cv2.threshold(img,127,255,0)
contours =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]

cnt=contours[0]
M=cv2.moments(cnt)
#centroid cordinates
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])
#area
area=cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)

cv2.circle(img,(cx,cy),2,(0,0,255),-1)



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(area)
print(perimeter)