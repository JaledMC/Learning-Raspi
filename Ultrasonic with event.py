#For precise measurement better use C. Remember use a resistor divisor for echo pin

#import libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIN_TRIGGER = 11
PIN_ECHO = 7
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

def trigger(PIN_TRIGGER):
    global pulse_start_time
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(11, GPIO.LOW)
    pulse_start_time = time.time()
    print(pulse_start_time)
    return 

def echo_event(PIN_TRIGGER):
    global distance
    pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    trigger(PIN_TRIGGER)
    return distance
     
def main():        
    # Setup trig and hecho pin
        
    GPIO.add_event_detect(PIN_ECHO, GPIO.RISING, callback=echo_event, bouncetime=100)
    
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print ("Waiting for sensor to settle")
    time.sleep(2)
    trigger(PIN_TRIGGER)
    
    pulse_start_time = 0
    distance = 0
    
    while True:
        #High to low level to activate trigger. Count time until echo receives the wave and goes high.
        #With the time and sound speed, obtain distance
        print ("Calculating distance")
        print ("Distance:",distance,"cm")
        time.sleep(0.5)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program...")
        pass
    finally:
        GPIO.cleanup()
