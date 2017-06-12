#!/usr/bin/python

import cv2
import numpy as np

#img = cv2.imread('circles.png', 1)

cam = cv2.VideoCapture(0)
s, img = cam.read() # captures image
#cv2.imshow("Test Picture", im) # displays captured image
cv2.imwrite("capture.bmp",img) # writes image test.bmp to disk


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([-5, 100, 100], dtype=np.uint8)
upper_range = np.array([15, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('mask',mask)
cv2.imshow('image', img)

while(1):
    k = cv2.waitKey(0)
    if(k == 27):
        break

cv2.destroyAllWindows()
