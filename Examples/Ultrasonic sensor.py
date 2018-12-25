#For precise measurement better use C. Remember use a resistor divisor for echo pin

#import libraries
import RPi.GPIO as GPIO
import time
     
def main():
    # Setup trig and hecho pin
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 11
    PIN_ECHO = 7
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print ("Waiting for sensor to settle")
    time.sleep(2)
    while True:
        #High to low level to activate trigger. Count time until echo receives the wave and goes high.
        #With the time and sound speed, obtain distance
        print ("Calculating distance")
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO)== 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)== 1:
            pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print ("Distance:",distance,"cm")
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program...")
        pass
    finally:
        GPIO.cleanup()


