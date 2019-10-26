# Opencv中的函数cv2.goodFeatureToTrack()用来进行Shi-Tomasi角点检测，其参数说明如下所示：
#
# 第一个参数：通常情况下，其输入的应是灰度图像；
#
# 第二个参数N：是想要输出的图像中N个最好的角点；
#
# 第三个参数：设置角点的质量水平，在0~1之间；代表了角点的最低的质量，小于这个质量的角点，则被剔除；
#
# 最后一个参数：设置两个角点间的最短欧式距离；也就是两个角点的像素差的平方和；
#
# 根据以上四个参数，运用此函数就能在图像上找到角点，所有低于质量水平的角点都被忽略；
# 然后再把质量水平合格的角点按照角点质量进行降序排列；首先选取质量最高的那个角点，将其欧式距离内的角点都删掉；
# 然后选取质量第二高的角点，重复进行；最后返回N个最佳角点；

# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pics/test.png')  # 原图为彩色图，可将第二个参数变为0，为灰度图

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 30, 0.3, 50)  # 返回的结果是 [[ a., b.]] 两层括号的数组。

corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 2, 255, -1)  # 在角点处画圆，半径为2，红色，线宽默认，利于显示
plt.imshow(img), plt.show()
