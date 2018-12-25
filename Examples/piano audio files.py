#Using callback functions to read buttons with software debounce. 02/10/2018

#import libraries
import RPi.GPIO as GPIO
from time import sleep
import pygame
pygame.init()
#Create a sound object with the file
my_sound = pygame.mixer.Sound('/home/pi/Desktop/Examples/audio.wav')

def button(channel):
    my_sound.play()
    return

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(7, GPIO.RISING, callback=button, bouncetime=300)
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