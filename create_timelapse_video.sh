#!/bin/bash

ffmpeg -framerate $1 -i $2 -c:v libx264 -r 20 -pix_fmt yuv420p out.mp4
