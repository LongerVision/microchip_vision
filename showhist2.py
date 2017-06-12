#!/usr/bin/python

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

for i in xrange(0,10):
    _, image = cam.read()

# Number of bins
LENGTH = 100
WIDTH = 100
HEIGHT = 100
bins = [LENGTH, WIDTH, HEIGHT];

# Range of bins
ranges = [0, 256, 0, 256, 0,256];
# Array of Image
images = [image];
# Number of channels
channels = [0, 1, 2];

#Calculate the Histogram
hist = cv2.calcHist(images, channels, None, bins, ranges);

# sortedIndex contains the indexes the
sortedIndex = np.argsort(hist.flatten());

# 1-D index of the max color in histogram
index = sortedIndex[-1]

# Getting the 3-D index from the 1-D index
k = index / (WIDTH * HEIGHT)
j = (index % (WIDTH * HEIGHT)) / WIDTH
i = index - j * WIDTH - k * WIDTH * HEIGHT

# Print the max RGB Value
print "Max RGB Value is = ", [i * 256 / HEIGHT, j * 256 / WIDTH, k * 256 / LENGTH]

r = i * 256 / HEIGHT
g = j * 256 / WIDTH
b = k * 256 / LENGTH

p=0.10

lower = np.array([b-(b*p),g-(g*p),r-(r*p)], dtype = "uint8")
upper = np.array([b+(b*p),g+(g*p),r+(r*p)], dtype = "uint8")
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)
