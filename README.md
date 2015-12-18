Pylapse
=======


Create timelapse using opencv,ffmpeg and python

Usage :
- to see a preview of the camera that you set to take the timelapse:
python pylapse.py --preview True


- to start a timelapse :
python pylapse.py -t True

for more help do python pylapse.py -h

notes:
- for now it uses opencv to get the images from the camera

- for now it uses ffmpeg to create the video after taking all the pictures
  if you don't have it installed you can download it from :
  https://www.ffmpeg.org/download.html

