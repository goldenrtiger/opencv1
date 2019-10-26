# coding=utf-8

# 前两个是必须的参数：
#
# 第一个参数是需要处理的图像；
# 第二个参数是图像的深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；
# 其后是可选的参数：
#
# dst不用解释了；
# ksize是算子的大小，必须为1、3、5、7。默认为1。
# scale是缩放导数的比例常数，默认情况下没有伸缩系数；
# delta是一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中；
# borderType是判断图像边界的模式。这个参数默认值为cv2.BORDER_DEFAULT。

import cv2
import numpy as np

img = cv2.imread("pics/test.png", 0)

gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(gray_lap)  # 转回uint8

cv2.imshow("orign", img)
cv2.imshow('laplacian', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()