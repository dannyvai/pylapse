Pylapse
=======


Create timelapse using opencv,ffmpeg and python

Usage :
- to see a preview of the camera that you set to take the timelapse:
python pylapse.py preview camera_idx height width

i.e
using camera 0 (/dev/video0) with img size of 640,480
python pylapse.py preview 0 480 640

- to start a timelapse :
python pylapse.py fps video_duration event_duration cam_idx height width
fps - frames per second of the output video
video_duration - the length of the video we take in seconds
event_duration - the amount of time we want to timelapse in seconds

for instance we want a 30 second video of sunset and the video will be 30fps
sunset is about 15 minutes from start to finish i guess so...
python pylapse.py 30 30 900 0 480 640

notes:
- for now it uses opencv to get the images from the camera

- for now it uses ffmpeg to create the video after taking all the pictures
  if you don't have it installed you can download it from :
  https://www.ffmpeg.org/download.html

