#Blink led example. 02/10/2018

#import libraries
import RPi.GPIO as GPIO
from time import sleep
# To use the GPIO pins two different numerations can be used: board(with the numerical position for each pin),
# and BCM, the special numeration of broadcom. But this last form is not the same for every raspberry model
GPIO.setmode(GPIO.BOARD)
#setup the 3 pin like output and low at initial state
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

def main():
    while True:
        GPIO.output(3, GPIO.HIGH)
        sleep(1)
        GPIO.output(3, GPIO.LOW)
        sleep(1)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program...")
        pass
    finally:
        GPIO.cleanup()
