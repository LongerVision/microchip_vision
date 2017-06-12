#!/usr/bin/python

from ast import literal_eval as make_tuple
import numpy as np
import argparse
import cv2

cam = cv2.VideoCapture(0)

for i in xrange(0,100):
    _, image = cam.read()

#cv2.imshow("images", image)

#cv2.waitKey(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

found = {}



def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))], max(v)

for x1 in xrange(0,180,1):
    for y1 in xrange(0,255,1):
        for z1 in xrange(0,255,1):

            for x2 in xrange(x1,180,1):
                for y2 in xrange(y1,255,1):
                    for z2 in xrange(z1,255,1):

                        lower = np.array([x1,y1,z1], dtype = "uint8")
                        upper = np.array([x2,y2,z2], dtype = "uint8")

                        mask = cv2.inRange(hsv, lower, upper)

                        output = cv2.bitwise_and(image, image, mask = mask)
                        cv2.imshow("images", np.hstack([image, output]))

                        if cv2.waitKey(1) & 0xFF is ord('q'):
                            exit

                        unmasked = cv2.countNonZero(mask)
                        if unmasked > 0:
                            #print unmasked, '(' + ','.join(map(str,[x,y,z])) + ')'
                            #found['(' + ','.join(map(str,[x,y,z])) + ')'] = unmasked
                            print unmasked, ' '.join(map(str,[x1,y1,z1, x2, y2, z2]))
                            found[' '.join(map(str,[x1,y1,z1, x2,y2,z2]))] = unmasked


#m = make_tuple(keywithmaxval(found))
k, v = keywithmaxval(found)
k = map(float, k.split())
print "k:", k, "v:", v

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

a, b = split_list(k)
lower = np.array(a, dtype = "uint8")
upper = np.array(b, dtype = "uint8")
mask = cv2.inRange(hsv, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)
