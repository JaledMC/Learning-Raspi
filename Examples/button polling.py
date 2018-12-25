#Blink led example.There are several ways of getting GPIO input into your program. The first and simplest way is to check the input
#value at a point in time. This is known as 'polling' and can potentially miss an input if your program reads the value at the wrong
#time. Polling is performed in loops and can potentially be processor intensive.  02/10/2018

#import libraries
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    while True:
        if(GPIO.input(7)):
            print("RED")
        if(GPIO.input(11) != 1):
            print("BLUE")
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program...")
        pass
    finally:
        GPIO.cleanup()#Blink led example. 02/10/2018