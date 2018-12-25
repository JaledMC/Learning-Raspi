from picamera import PiCamera
from time import sleep
camera = PiCamera()

"""You can use camera.awb_mode to set the auto white balance to a
preset mode to apply a particular effect. The options are: off,
auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent,
flash, and horizon."""

camera.start_preview()
for mode in camera.AWB_MODES:
    camera.awb_mode = mode
    camera.annotate_text = "Effect: %s" % mode
    sleep(5)
camera.stop_preview()

