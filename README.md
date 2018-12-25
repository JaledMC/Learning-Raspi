# Learning-Raspi
Learning electronic and programming with Raspberry Pi

# [Raspberry setup]()

# Code examples
    Digital write: 
* [Led blink]()
* [Knight rider]()
* [Buttons polling]()
https://projects.raspberrypi.org/en/projects/python-quick-reaction-game
https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
* [Interruptions](https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/)

* [HC-SR04](https://projects.raspberrypi.org/en/projects/see-like-a-bat): For precise measurement better use C. Remember use a resistor divisor for echo pin
https://www.instructables.com/id/The-Raspberry-Pi-Arduino-Connection/
* [Keyboard](): Install the library with sudo pip3 install pad4pi

Sounds
https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/code
Play sounds on RBpi with a piezo hasn’t much sense because the easiest way is use pwm and with it loses jack audio output. One way is use audio [utils](https://raspberrypi-aa.github.io/session3/audio.html), [2](https://www.olivieraubert.net/vlc/python-ctypes/), [vlc](https://www.instructables.com/id/The-Raspberry-Pi-Arduino-Connection/), or piGame, to play audio files. We can synthesize midi audio with Sonic pi, or PyGame midi.
    [Piano](https://projects.raspberrypi.org/en/projects/gpio-music-box)
Theremin with Sonic pi communication
https://projects.raspberrypi.org/en/projects/ultrasonic-theremin
Theremin with pygame synthesis
http://www.derickdeleon.com/2014/07/midi-based-theremin-using-raspberry-pi.html
* [Accelerometer](https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-14-adxl345-super-kit-for-raspberrypi.html)

https://www.instructables.com/id/The-Raspberry-Pi-Arduino-Connection/
https://www.prometec.net/raspberry-puertas-analogicas/

Camera
https://www.pyimagesearch.com/2016/01/04/unifying-picamera-and-cv2-videocapture-into-a-single-class-with-opencv/
https://picamera.readthedocs.io/en/release-1.13/

https://projects.raspberrypi.org/en/projects/the-all-seeing-pi
    https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
    Enable camera un pi config and connect the ribbon cable to the camera connector, not the display
    the camera preview only works when a monitor is connected to the Pi, so remote access (such as SSH and VNC) will not allow you to see the camera preview
    https://picamera.readthedocs.io/en/release-1.13/
    Use picamera and usb-camera
We can reproduce the video from terminal with omxplayer. If you need to exit the fullscreen video, use Alt+F4
PWMGPIO 12/13/18/19 all have hardware PWM and are available (pins 32/33/12/35). However 12/18 share a setting as do 13/19.
    PWM: dimmer
    SoftPWM: RGB
[Serial](https://pimylifeup.com/raspberry-pi-serial/)
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
    [Android GPIO Control](https://circuitdigest.com/microcontroller-projects/controlling-raspberry-pi-gpio-using-android-app-over-bluetooth)
SIM800L
    
    



# Projects
* [Kodi Media Center](https://pimylifeup.com/raspberry-pi-xbmc-media-center/)
* [Arcade machine](https://www.youtube.com/watch?v=psWCmLwvWBE)    
https://pimylifeup.com/raspberry-pi-dosbox/
* [Kiosk](https://pimylifeup.com/raspberry-pi-kiosk/)
* [Smart Mirror](https://hackaday.io/project/13466-raspberry-pi-smart-mirror)
https://magicmirror.builders/
* []()
* [Robot](https://www.instructables.com/id/Raspberry-Pi-Web-Controlled-Autonomous-Robot/)
* [Weather station]()
https://projects.raspberrypi.org/en/projects/temperature-log
* [Web](https://www.instructables.com/id/Simple-and-intuitive-web-interface-for-your-Raspbe/)
* [TOR access point](https://pimylifeup.com/raspberry-pi-tor-access-point/)
* [VPN](https://pimylifeup.com/raspberry-pi-vpn-access-point/)
* [Web Server](https://pimylifeup.com/raspberry-pi-nginx/)
https://pimylifeup.com/raspberry-pi-web-server/
https://pimylifeup.com/raspberry-pi-plex-server/

* [Telegram](https://pimylifeup.com/raspberry-pi-telegram-bot/)
* [Cloud](https://pimylifeup.com/raspberry-pi-owncloud/)

* [Pirate radio](https://pimylifeup.com/raspberry-pi-pirate-radio/)
* [Webcam server]()
* [Time lapse]()
* [Camera detection]()
* [Twitter Bot](https://pimylifeup.com/raspberry-pi-twitter-bot/)
* [Alexa](https://pimylifeup.com/raspberry-pi-alexa/)
* [Google assistant](https://pimylifeup.com/raspberry-pi-google-assistant/)

    
    



https://projects.raspberrypi.org/en/projects/the-all-seeing-pi



Programs
    Python image
    Excel





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


# References
* [Hackster](https://www.hackster.io/raspberry-pi/projects?sort=trending&page=3)
* [Pimylifeup](https://pimylifeup.com/)
* [pyimagesearch](https://www.pyimagesearch.com/)
* [raspberrypi.org](https://projects.raspberrypi.org/en)
