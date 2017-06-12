#!/usr/bin/python

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cam = cv2.VideoCapture(0)
_, image = cam.read() # captures image
cv2.imwrite("capture.bmp",image) # writes image test.bmp to disk

image = cv2.medianBlur(image, 3)

# define the list of boundaries
boundaries = [
    #([17, 15, 100], [50, 56, 200]),
    #([30, 150, 50], [255, 255, 180]),
    #([86, 31, 4], [220, 88, 50]),
    #([25, 146, 190], [62, 174, 250]),
    ([35, 100, 100], [40, 255, 255]),
    ([59, 100, 100], [79, 255, 255])
    #([103, 86, 65], [145, 133, 128])
    #([110, 50, 50], [130, 255, 255])
    ]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    #accumMask = cv2.bitwise_not(mask)
    unmasked = cv2.countNonZero(mask)
    print unmasked


    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    #cv2.imshow('mask', mask)
    cv2.waitKey(0)
