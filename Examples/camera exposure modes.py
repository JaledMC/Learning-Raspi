from picamera import PiCamera
from time import sleep
camera = PiCamera()

"""You can use camera.exposure_mode to set the exposure to a preset mode to
apply a particular effect. The options are: off, auto, night, nightpreview,
backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake,
and fireworks."""
camera.start_preview()
for exposure in camera.EXPOSURE_MODES:
    camera.exposure_mode = exposure
    camera.annotate_text = "Effect: %s" % exposure
    sleep(5)
camera.stop_preview()