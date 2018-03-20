#Drawing on the image and writing on the image
import numpy as np
import cv2
img=cv2.imread('mom.JPG',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(100,100),(255,255,255),6)
#(where to draw,starting_point,ending_point,color,thickness)
cv2.rectangle(img,(15,25),(200,150),(0,0,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)
#center,radius,color,opaque

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts=pts.reshape((-1,1,2))-->in documentation we ignore
cv2.polylines(img,[pts],True,(0,255,255),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'LABEL',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()