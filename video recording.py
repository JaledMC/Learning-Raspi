from picamera import PiCamera
from time import sleep
camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

# we can see the video file with $omxplayer video_name
