from gpiozero import DistanceSensor
from time import sleep

#BCM pin style
sensor = DistanceSensor(echo=17, trigger=4)

while True:
    print(sensor.distance)
    sleep(1)