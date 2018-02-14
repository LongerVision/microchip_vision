![Microchip](docs/microchip_logo.png)

# Microchip Machine Vision Demo Application

This is a simple demo written using Python that uses OpenCV to perform machine
vision recognition of different colored objects.  It will identify and display
the color of the object.

## Dependencies

- Python 2
- OpenCV 3
- PyQt5

## Requirements

The demo will work with any Video4Linux (V4L) device such as a webcam.

## Running

In some environments, it may be necessary to specify an alternate GTK theme to
use.

    QT_QPA_PLATFORMTHEME=gtk2 ./detect.py


## License

Microchip Machine Vision Demo is released under the terms of the `GPLv3`
license. See the `COPYING` file for more information.
