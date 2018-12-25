#led dimmer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
led = GPIO.PWM(18, 100) # pin, freq
led.start(100)    #init duty

while True:
    for i in range(100,-1,-1):
        led.ChangeDutyCycle(100 - i)
        time.sleep(0.02)           
    print("Loop ended")