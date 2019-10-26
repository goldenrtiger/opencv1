# OpenCV中的角点检测
# 使用 cv2.cornerHarris()，参数如下：
#
# 　　img：数据类型为float32的输入图像（灰度图）
#
# 　　blockSize：角点检测中要考虑的领域大小
#
# 　　ksize：Sobel求导中使用的窗口大小
#
# 　　k：Harris角点检测方程中的自由参数，取值参数为[0.04，0.06]
import cv2
import numpy as np

img = cv2.imread('pics/test.png')

# 1. Harris角点检测基于灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Harris角点检测
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
# 腐蚀一下，便于标记
dst = cv2.dilate(dst, None)

# 角点标记为红色
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imwrite('blox-RedPoint.png', img)
cv2.imshow('dst', img)
cv2.waitKey(0)