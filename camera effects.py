from picamera import PiCamera
from time import sleep
camera = PiCamera()

# We can modify many effects with camera.image_effect = 'colorswap'

"""Options: none, negative, solarize, sketch, denoise, emboss, oilpaint,
    hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap,
    washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1,
    and deinterlace2"""

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
camera.stop_preview()