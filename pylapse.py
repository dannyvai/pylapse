import cv2

import time
import sys,os


def init_cam(device_id,width,height):
    cam = cv2.VideoCapture(device_id)
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)
    return cam

#######
# fps - the fps of the output movie (hz)
#video_duration - the length of the output movie (sec)
#event_duration - the duration of the event that you want to capture (sec)
#cam_idx - the camera idx (if only one camera it should be  0)
#height - the image height in pixels
#width - the image width in pixels
#######
def start_timelapse(fps,video_time,event_duration,cam_idx,height,width) :

    cam = init_cam(cam_idx,width,height)
    timelapse_sleep  = float(event_duration) /  float(fps * video_time) 
    idx = 1
    max_frame_id = event_duration / timelapse_sleep
    image_name_format = "%c0%dd.png" % ('%',len(str(max_frame_id)))
    tic = time.time()
    while idx < max_frame_id:
        s, img_rgb = cam.read()
        img_name = image_name_format % idx
        cv2.imwrite(img_name,img_rgb)
        time.sleep(timelapse_sleep)
        idx = idx + 1

        if time.time() - tic > 5:
            print 'created %d images out of %d' %(idx,max_frame_id)
            tic = time.time()
            
    os.system('ffmpeg -framerate %d -i %s -c:v libx264 -r 20 -pix_fmt yuv420p out.mp4' % (fps,image_name_format))

def preview_cam(cam_idx,height,width):
    cam = init_cam(cam_idx,width,height)
    print cam_idx,width,height
    while(True):
        # Capture frame-by-frame
        ret, frame = cam.read()
    
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()

def main():

    if len(sys.argv) > 1 :
        if sys.argv[1] == "preview" :
            if len(sys.argv) < 5:
                print 'Usage %s preview camera_idx height width' % sys.argv[0]
                exit(1)
            cam_idx = int(sys.argv[2])
            height = int(sys.argv[3])
            width = int(sys.argv[4])
            preview_cam(cam_idx,height,width)
            
        if sys.argv[1] == "timelapse" and len(sys.argv) >=  8 :
            try :
                fps = int(sys.argv[2])
                video_time = int(sys.argv[3])
                event_duration = int(sys.argv[4])
                cam_idx = int(sys.argv[5])
                height = int(sys.argv[6])
                width = int(sys.argv[7])
            except :
                print 'Usage %s timelapse fps(int) video_duration(int) event_duration(int) cam_idx height width' % sys.argv[0]
                exit(1)
            start_timelapse(fps,video_time,event_duration,cam_idx,height,width)
        else :
            print 'Usage %s timelapse fps(int) video_time(int) event_duration(int) cam_idx height width' % sys.argv[0]
    else :
            print 'Usage %s timelapse fps(int) video_time(int) event_duration(int) cam_idx height width' % sys.argv[0]
            print 'Usage %s preview cam_idx height width' % sys.argv[0]
if __name__ == "__main__":
    main()