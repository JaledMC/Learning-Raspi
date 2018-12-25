#Blink leds and make effects 02/10/2018
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

def blink_led(led, delay):
    ms = delay/1000
    GPIO.output(led, GPIO.HIGH)
    sleep(ms)
    GPIO.output(led, GPIO.LOW)
    sleep(ms)
    return

def bling_bling():
    blink_led(3, delay)
    blink_led(5, delay)
    blink_led(7, delay)
    blink_led(11, delay)
    
def vumeter(delay):
    ms = delay/1000
    GPIO.output(3, GPIO.HIGH)
    sleep(ms)
    GPIO.output(5, GPIO.HIGH)
    sleep(ms)
    GPIO.output(7, GPIO.HIGH)
    sleep(ms)
    GPIO.output(11, GPIO.HIGH)
    sleep(ms)
    GPIO.output(11, GPIO.LOW)
    sleep(ms)
    GPIO.output(7, GPIO.LOW)
    sleep(ms)
    GPIO.output(5, GPIO.LOW)
    sleep(ms)
    GPIO.output(3, GPIO.LOW)
    sleep(ms)

def main():
    delay = 100
    while True:
        vumeter(delay)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program...")
        pass
    finally:
        GPIO.cleanup()