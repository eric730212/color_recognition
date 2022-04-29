import cv2
import numpy as np

img_bgr = cv2.imread('pic/color5.jpg')
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
thresh1 = np.array([0,155,93])
thresh2 = np.array([97,255,255])
img_flag = cv2.inRange(img_hsv,thresh1,thresh2)

img_morph = img_flag.copy()
"""cv2.erode(img_morph,(3,3),img_morph,iterations=3)
cv2.dilate(img_morph,(3,3),img_morph,iterations=3)"""

cnts,_ = cv2.findContours(img_morph,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts_sort = sorted(cnts, key= cv2.contourArea,reverse=True)
box = cv2.minAreaRect(cnts_sort[0])
points = np.int0(cv2.boxPoints(box))

cen_v = (points[0,0] + points[2,0])/2
cen_h = (points[0,1]+points[2,1])/2
rows ,cols =img_bgr.shape[:2]
print('color : ('+str(cols)+','+str(rows)+')')
print('center : ('+str(cen_h)+','+str(cen_v)+')')

cv2.drawContours(img_bgr,[points],-1,(255,0,0),2)

cv2.imshow('original',img_bgr)
cv2.imshow('red',img_flag)
cv2.imshow('morph',img_morph)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()