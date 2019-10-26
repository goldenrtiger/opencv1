#Canny边缘提取

# OpenCV的Canny函数用于在图像中查找边缘，其函数原型有两种：
# #
# # ①直接调用Canny算法在单通道灰度图像中查找边缘，
# #
# # 其函数原型为：Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) -> edges
# #
# # image参数表示8位输入图像。
# #
# # threshold1参数表示设置的低阈值。
# #
# # threshold2参数表示设置的高阈值，一般设定为低阈值的3倍 (根据Canny算法的推荐)。
# #
# # edges参数表示输出边缘图像，单通道8位图像。
# #
# # apertureSize参数表示Sobel算子的大小。
# #
# # L2gradient参数表示一个布尔值，如果为真，则使用更精确的L2范数进行计算（即两个方向的倒数的平方和再开方），否则使用L1范数（直接将两个方向导数的绝对值相加）。
# #
# # ②使用带自定义图像渐变的Canny算法在图像中查找边缘，
# #
# # 其函数原型为：Canny(dx, dy, threshold1, threshold2[, edges[, L2gradient]]) -> edges
# #
# # dx参数表示输入图像的x导数（x导数满足16位，选择CV_16SC1或CV_16SC3）
# #
# # dy参数表示输入图像的y导数（y导数满足16位，选择CV_16SC1或CV_16SC3）。
# #
# # threshold1参数表示设置的低阈值。
# #
# # threshold2参数表示设置的高阈值，一般设定为低阈值的3倍 (根据Canny算法的推荐)。
# #
# # edges参数表示输出边缘图像，单通道8位图像。
# #
# # L2gradient参数表示L2gradient参数表示一个布尔值，如果为真，则使用更精确的L2范数进行计算（即两个方向的倒数的平方和再开方），否则使用L1范数（直接将两个方向导数的绝对值相加）。

import cv2 as cv
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    # xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0) #x方向梯度
    # ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1) #y方向梯度
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    dst = cv.bitwise_and(image, image, mask= edge_output)
    cv.imshow("Color Edge", dst)
src = cv.imread('pics/test.png')
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()