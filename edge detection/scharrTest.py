import cv2
import sys
import numpy as np


o=cv2.imread("pics/test.png",cv2.IMREAD_GRAYSCALE)

scharrx=cv2.Scharr(o,cv2.CV_64F,1,0)
scharry=cv2.Scharr(o,cv2.CV_64F,0,1)
scharrx=cv2.convertScaleAbs(scharrx)
scharry=cv2.convertScaleAbs(scharry)

scharrxy=cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

cv2.imshow("scharrx",scharrx)
cv2.imshow("scharry",scharry)
cv2.imshow("scharrxy",scharrxy)

cv2.waitKey(0)
