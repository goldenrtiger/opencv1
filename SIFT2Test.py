# cv2.drawKeypoints:
# image:也就是原始图片
# keypoints：从原图中获得的关键点，这也是画图时所用到的数据
# outputimage：输出
# color：颜色设置，通过修改（b,g,r）的值,更改画笔的颜色，b=蓝色，g=绿色，r=红色。

# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
#
# imgname1 = 'pics/test.png'
# imgname2 = 'pics/test3.png'
#
# surf = cv2.xfeatures2d.SURF_create()
#
# FLANN_INDEX_KDTREE = 0
# index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
# search_params = dict(checks=50)
# flann = cv2.FlannBasedMatcher(index_params,search_params)
#
# img1 = cv2.imread(imgname1)
# gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #灰度处理图像
# kp1, des1 = surf.detectAndCompute(img1,None)#des是描述子
#
# img2 = cv2.imread(imgname2)
# gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# kp2, des2 = surf.detectAndCompute(img2,None)
#
# hmerge = np.hstack((gray1, gray2)) #水平拼接
# cv2.imshow("gray", hmerge) #拼接显示为gray
# cv2.waitKey(0)
#
# img3 = cv2.drawKeypoints(img1,kp1,img1,color=(255,0,255))
# img4 = cv2.drawKeypoints(img2,kp2,img2,color=(255,0,255))
#
# hmerge = np.hstack((img3, img4)) #水平拼接
# cv2.imshow("point", hmerge) #拼接显示为gray
# cv2.waitKey(0)
#
# matches = flann.knnMatch(des1,des2,k=2)
#
# good = []
# for m,n in matches:
#     if m.distance < 0.7*n.distance:
#         good.append([m])
# img5 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
# cv2.imshow("SURF", img5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import numpy as np
import cv2
from matplotlib import pyplot as plt

imgname1 = 'pics/test.png'
imgname2 = 'pics/test4.png'

sift = cv2.xfeatures2d.SIFT_create()

# FLANN 参数设计
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)

img1 = cv2.imread(imgname1)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #灰度处理图像
kp1, des1 = sift.detectAndCompute(img1,None)#des是描述子

img2 = cv2.imread(imgname2)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
kp2, des2 = sift.detectAndCompute(img2,None)

hmerge = np.hstack((gray1, gray2)) #水平拼接
cv2.imshow("gray", hmerge) #拼接显示为gray
cv2.waitKey(0)

img3 = cv2.drawKeypoints(img1,kp1,img1,color=(255,0,255))
img4 = cv2.drawKeypoints(img2,kp2,img2,color=(255,0,255))

hmerge = np.hstack((img3, img4)) #水平拼接
cv2.imshow("point", hmerge) #拼接显示为gray
cv2.waitKey(0)
matches = flann.knnMatch(des1,des2,k=2)
matchesMask = [[0,0] for i in range(len(matches))]

good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
    # if m.distance < 1*n.distance:
        good.append([m])

# img5 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,flags=2)
img5 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
cv2.imshow("FLANN", img5)
cv2.waitKey(0)
cv2.destroyAllWindows()