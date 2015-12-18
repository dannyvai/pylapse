import cv2
import time
import sys,os
from optparse import OptionParser

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
def start_timelapse(fps,video_time,event_duration,cam_idx,height,width,output_dir,quality) :

    cam = init_cam(cam_idx,width,height)
    timelapse_sleep  = float(event_duration) /  float(fps * video_time) 
    idx = 1
    max_frame_id = event_duration / timelapse_sleep
    image_name_format = "%s/%c0%dd.jpg" % (output_dir,'%',len(str(max_frame_id)))
    tic = time.time()
    while idx < max_frame_id:
        s, img_rgb = cam.read()
        img_name = image_name_format % idx
        cv2.imwrite(img_name,img_rgb,[int(cv2.IMWRITE_JPEG_QUALITY), quality])
        time.sleep(timelapse_sleep)
        idx = idx + 1

        #debug print to see some progress
        if time.time() - tic > 5:
            print 'created %d images out of %d' %(idx,max_frame_id)
            tic = time.time()
            
    os.system('ffmpeg -framerate %d -i %s -c:v libx264 -r 20 -pix_fmt yuv420p %s/%d.mp4' % (fps,image_name_format,output_dir,int(time.time())))

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

    parser = OptionParser()

    parser.add_option("-p", "--preview", dest="preview",
                      default=False,
                      help="Preview the camera")
    parser.add_option("-t", "--timelapse",
                      default=False,
                      help="start taking pictures for the timelapse")
    parser.add_option("-w", "--width",
                      default=640,
                      help="camera image width in pixels")
    parser.add_option("-l", "--height",
                      default=480,
                      help="camera image height in pixels")
    parser.add_option("-c", "--cam_idx",
                      default=0,
                      help="camera index")
    parser.add_option("-f", "--fps",
                      default=30,
                      help="video output fps")
    parser.add_option("-v", "--video-duration",
                      default=10,
                      help="output video duration")
    parser.add_option("-e", "--event-duration",
                      default=120,
                      help="event duration (how much time the event is going to take)")
    parser.add_option("-o", "--output-dir",
                      default='./',
                      help="the folder it would create the images and the video")
    parser.add_option("-q", "--quality",
                      default=90,
                      help="image quality of the compression")

    (options, args) = parser.parse_args()
    
    output_dir = options.output_dir    
    if os.path.isdir(output_dir) == False:
        print "%s doesn't exist please choose another folder" % output_dir
        exit(0)

    cam_idx = int(options.cam_idx)
    height = int(options.height)
    width = int(options.width)
    
    if bool(options.preview):
        preview_cam(cam_idx,height,width)
        
    elif bool(options.timelapse):
        fps = int(options.fps)
        video_duration = int(options.video_duration)
        event_duration = int(options.event_duration)
        quality = int(options.quality)
        start_timelapse(fps,video_duration,event_duration,cam_idx,height,width,output_dir,quality)
        
if __name__ == "__main__":
    main()