# use ls /dev/tty* to detect the arduino port
import serial
import time

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

while True:
    val = arduino.readline()
    print(val)
arduino.close()