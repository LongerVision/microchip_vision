#!/usr/bin/python

import numpy as np
import argparse
import cv2

cam = cv2.VideoCapture(0)
boundary = ([35, 100, 100], [40, 255, 255])

while (1):

    _, image = cam.read()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array(boundary[0], dtype = "uint8")
    upper = np.array(boundary[1], dtype = "uint8")

    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    #accumMask = cv2.bitwise_not(mask)
    unmasked = cv2.countNonZero(mask)
    print unmasked

    cv2.imshow("images", np.hstack([image, output]))

    k = cv2.waitKey(0)
    print "key " , k
    if k == 113:
        boundary[0][0] = boundary[0][0] + 1
        boundary[1][0] = boundary[1][0] + 1
        print boundary
    elif k == 97:
        boundary[0][0] = boundary[0][0] - 1
        boundary[1][0] = boundary[1][0] - 1
        print boundary
    elif k == 119:
        boundary[0][1] = boundary[0][1] + 1
        boundary[1][1] = boundary[1][1] + 1
        print boundary
    elif k == 115:
        boundary[0][1] = boundary[0][1] - 1
        boundary[1][1] = boundary[1][1] - 1
        print boundary
    elif k == 101:
        boundary[0][2] = boundary[0][2] + 1
        boundary[1][2] = boundary[1][2] + 1
        print boundary
    elif k == 100:
        boundary[0][2] = boundary[0][2] - 1
        boundary[1][2] = boundary[1][2] - 1
        print boundary
    elif k == 65361:
        boundary[0][0] = boundary[0][0] + 1
        boundary[1][0] = boundary[1][0] - 1
        print boundary
    elif k == 65363:
        boundary[0][0] = boundary[0][0] - 1
        boundary[1][0] = boundary[1][0] + 1
        print boundary
    elif k == 27:
        break
