#!/usr/bin/env python

#
# Joshua Henderson <joshua.henderson@microchip.com>
# Detect colors from a camera and identify it once the mask is big enough.
#

import cv2
import argparse
import numpy as np
from operator import xor
from PyQt5 import QtWidgets

boundaries = [
    ([8.5, 100, 100], [23, 255, 255], "orange"),
    ([30, 100, 100], [35, 255, 255], "yellow"), # 32
    ([97, 100, 100], [117, 255, 255], "blue"),
    ([57, 100, 100], [77, 255, 255], "green"),
    ([153, 100, 100], [173, 255, 255], "pink"),
    ([24, 100, 100], [26, 255, 255], "dark yellow"), # 25
    ([0, 100, 100], [7, 255, 255], "red1"),
    ([175, 100, 100], [180, 255, 255], "red2"),
    ]

font = cv2.FONT_HERSHEY_SIMPLEX

def main(seperate, contour, fullscreen=False):

    camera = cv2.VideoCapture(0)

    # can you say unstable API?
    if hasattr(cv2, 'cv'):
        if fullscreen:
            cv2.namedWindow("images", cv2.cv.CV_WINDOW_NORMAL | cv2.cv.CV_WINDOW_KEEPRATIO)
            cv2.setWindowProperty("images", cv2.cv.CV_WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
            geometry = QtWidgets.QDesktopWidget().screenGeometry(-1)
            cv2.resizeWindow("images", geometry.width(), geometry.height())

        camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
        camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
    else:
        if fullscreen:
            cv2.namedWindow("images", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
            cv2.setWindowProperty("images", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            geometry = QtWidgets.QDesktopWidget().screenGeometry(-1)
            cv2.resizeWindow("images", geometry.width(), geometry.height())

        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    ret, image = camera.read()
    if not ret:
        print "error: failed to read image from camera"
        return

    height, width = image.shape[:2]
    black = np.zeros((height,width,3), np.uint8)

    while True:
        ret, image = camera.read()
        if not ret:
            print "error: failed to read image from camera"
            break

        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        unmasked = 0
        for (lower, upper, name) in boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")

            mask = cv2.inRange(frame_to_thresh, lower, upper)
            output = cv2.bitwise_and(image, image, mask = mask)

            unmasked = cv2.countNonZero(mask)
            if unmasked > (height * width / 10):
                cv2.putText(output, str(name), (100,100), font, 1, (255,255,255), 2)

                if contour:
                    _, contours, hierarchy = cv2.findContours(mask.copy(),
                                                              cv2.RETR_EXTERNAL,
                                                              cv2.CHAIN_APPROX_SIMPLE)
                    for i, c in enumerate(contours):
                        area = cv2.contourArea(c)
                        if area > 1000:
                            cv2.drawContours(output, contours, i, (0, 255, 0), 3)

                break

        if unmasked > (height * width / 10):
            if not seperate:
                cv2.imshow("images", output)
            else:
                cv2.imshow("images", np.hstack([image, output]))
        else:
            if not seperate:
                cv2.imshow("images", image)
            else:
                cv2.imshow("images", np.hstack([image, black]))

        cv2.setWindowProperty("images", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        key = cv2.waitKey(10) & 0xFF
        if key is ord('q'):
            break
        elif key is ord('0'):
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Detect Colors.')
    parser.add_argument('-c', '--contour',
                        help='Show a contour around color mask',
                        action='store_true')
    parser.add_argument('-s', '--seperate',
                        help='Seperate video feed and color mask images',
                        action='store_true')
    parser.add_argument('-f', '--fullscreen',
                        help='Show window in fullscreen mode',
                        action='store_true')
    args = parser.parse_args()
    main(args.seperate, args.contour, args.fullscreen)
