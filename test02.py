import cv2
import numpy as np

img_original = cv2.imread('pic/color.jpg')
# 转变为HSV颜色空间
img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
# 返回黄色区域的二值图像
img_yellow = cv2.inRange(img_original, (27, 160, 215), (83, 255, 255))
##输入图像与输入图像在掩模条件下按位与，得到掩模范围内的原图像
img_specifiedColor = cv2.bitwise_and(img_original, img_original, mask=img_yellow)
cv2.imshow('img_yellow', img_specifiedColor)
cv2.waitKey()
cv2.destroyAllWindows()
