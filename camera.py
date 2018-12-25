from picamera import PiCamera
from time import sleep
camera = PiCamera()

# We can adjust the camera resolution. Max resolution for video is 1920 x 1080 and
# 2592x1944 for photos. The maximun frame rate in that case is camera.framerate = 15
# minimun resolution is 64x64

# We can rotate the image 0, 90, 180 or 270 degrees with camera.rotation = 180
# we can modify transparency between 0 to 255 like this camera.start_preview(alpha=200)

#camera.start_preview()
camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
sleep(10)
camera.stop_preview()