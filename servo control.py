#servo control
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
led = GPIO.PWM(18, 50) # 50Hz
led.start(7.5)    

#right
led.ChangeDutyCycle(10.5)
time.sleep(5)
#stop
led.ChangeDutyCycle(7.5)
time.sleep(5)
#left
led.ChangeDutyCycle(4.5)
time.sleep(5)