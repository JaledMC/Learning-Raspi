# Learning-Raspi
Learning electronic and programming with Raspberry Pi

# References
    * [Hackster](https://www.hackster.io/raspberry-pi/projects?sort=trending&page=3)
    * [Pimylifeup](https://pimylifeup.com/)
    * [pyimagesearch](https://www.pyimagesearch.com/)
    * [raspberrypi.org](https://projects.raspberrypi.org/en)

* [Raspberry setup]()
* []()



# Code examples
    Digital write: 
* [Led blink]()
* [Knight rider]()
* [Buttons polling]()
* [Interruptions]()
* [HC-SR04](): For precise measurement better use C. Remember use a resistor divisor for echo pin
* [Keyboard](): Install the library with sudo pip3 install pad4pi

Sounds
Play sounds on RBpi with a piezo hasn’t much sense because the easiest way is use pwm and with it loses jack audio output. One way is use audio utils, 2, vlc, or piGame, to play audio files. We can synthesize midi audio with Sonic pi, or PyGame midi.
    Piano
Theremin with Sonic pi communication
Theremin with pygame synthesis
* [Accelerometer]()


Camera
    https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
    Enable camera un pi config and connect the ribbon cable to the camera connector, not the display
    the camera preview only works when a monitor is connected to the Pi, so remote access (such as SSH and VNC) will not allow you to see the camera preview
    https://picamera.readthedocs.io/en/release-1.13/
    Use picamera and usb-camera
We can reproduce the video from terminal with omxplayer. If you need to exit the fullscreen video, use Alt+F4
PWMGPIO 12/13/18/19 all have hardware PWM and are available (pins 32/33/12/35). However 12/18 share a setting as do 13/19.
    PWM: dimmer
    SoftPWM: RGB
Serial
    Enabling I2C, SPI and others
Install i2c tools to know the devices address
sudo apt-get install i2c-tools
        Install smbus to use i2c pins and reboot
apt-get install python-smbus
        I2C / UART
        Arduino usb
ADC
    ADS1115
    POT  
    Trimmer
    LDR
    Displays
        LCD 1620
            $ sudo pip3 install RPLCD
        Screen
        Touchscreen
Bluetooth
    Android GPIO Control
SIM800L
    
    



# Projects
* [Kodi Media Center]()
* [Arcade machine]()
* [Kiosk]()
* [Smart Mirror]()
* []()
* [Robot]()
* [Weather station]()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* [Webcam server]()
* [Time lapse]()
* [Camera detection]()
* [Face recognition]()
* [Twitter Bot]()
* [Alexa]()
* [Google assistant]()

    
    



https://projects.raspberrypi.org/en/projects/the-all-seeing-pi



Programs
    Python image
    Excel

Web
TOR access point
VPN
Web Server
Server
Server
    Personal Cloud
Pirate Radio
Telegram


https://maker.pro/raspberry-pi/projects/raspberry-pi-web-server
Temperature log

SMS
https://projects.raspberrypi.org/en/projects/python-quick-reaction-game/7
Program via web

[raspberry fan gpios initialization](https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c)
