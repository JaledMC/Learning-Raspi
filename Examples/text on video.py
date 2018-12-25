from picamera import PiCamera, Color
from time import sleep
camera = PiCamera()

camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
# sizes from 6 to 160. 32 default
camera.annotate_text_size = 50
camera.annotate_text = "Hola Fonso!"

camera.start_preview()
sleep(10)
camera.stop_preview()

