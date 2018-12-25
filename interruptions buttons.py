#Using callback functions to read buttons with software debounce. 02/10/2018

#import libraries
import RPi.GPIO as GPIO
from time import sleep

def one(channel):
    print("One")
    return
def two(channel):
    print("Two")
    return

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(7, GPIO.RISING, callback=one, bouncetime=300)
    GPIO.add_event_detect(11, GPIO.FALLING, callback=two, bouncetime=300)
    #To remove events use "GPIO.remove_event_detect(channel)"
    while True:
        sleep(1) # Nothing to do here
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program...")
        pass
    finally:
        GPIO.cleanup()