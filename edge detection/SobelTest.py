# coding=utf-8

# 前四个是必须的参数：
#
# 第一个参数是需要处理的图像；
# 第二个参数是图像的深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；
# dx和dy表示的是求导的阶数，0表示这个方向上没有求导，一般为0、1、2。
# 其后是可选的参数：
#
# dst不用解释了；
# ksize是Sobel算子的大小，必须为1、3、5、7。
# scale是缩放导数的比例常数，默认情况下没有伸缩系数；
# delta是一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中；
# borderType是判断图像边界的模式。这个参数默认值为cv2.BORDER_DEFAULT。

import cv2
import numpy as np

img = cv2.imread("pics/test.png", 0)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x) # 转回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("absX", absX)
cv2.imshow("absY", absY)

cv2.imshow("Result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()