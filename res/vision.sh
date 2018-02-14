#!/bin/sh

eval "$DEMO_LEAVE"

cd "$(dirname "$0")"
./detect.py -f -s

eval "$DEMO_ENTER"
