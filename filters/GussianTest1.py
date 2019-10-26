# coding: utf-8
import numpy as np
import cv2

img = cv2.imread('pics/test.png')
img_ = cv2.GaussianBlur(img, ksize=(9, 9), sigmaX=0, sigmaY=0)

cv2.imshow('Source image', img)
cv2.imshow('blur image', img_)
cv2.waitKey()
