import cv2
import numpy as np
#载入原图
img_original=cv2.imread('pic/color.jpg')
#转变为HSV颜色空间
img_hsv=cv2.cvtColor(img_original,cv2.COLOR_BGR2HSV)
#返回黄色区域的二值图像
img_yellow=cv2.inRange(img_original,(27,160,215),(83,255,255))
cv2.imshow('img_original',img_original)
cv2.imshow('img_target',img_yellow)
cv2.waitKey()
cv2.destroyAllWindows()