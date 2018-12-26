# Learning-Raspi
Learning electronic and programming with Raspberry Pi  

# Raspberry setup
The easiest way to run with raspberry is installing NOOBS in a FAT32 SD. Other OS like Ubuntu Mate, Raspbian, or Chromium are valid too. PD: At present, all OS are 32 bits.   

First step must be change default password, for security reasons, like ssh access. Use “sudo passwd” command. Username: pi Password: raspberry  

Later, update the system:
`sudo apt-get update`  
`sudo apt-get upgrade`  

If raspbian freezes, disconnect usbs and HDMi can help. Disconnect supply could corrupt system files. Use ctrl+alt+f1 to switch to kernel, and use sudo reboot. To return to GUI, use ctrl+alt+f7.    

For **Arduino installation**:  
`sudo apt-get install arduino`  

For **Opencv installation**: 
`sudo apt-get install libhdf5-dev libhdf5-serial-dev`  
`sudo apt-get install libqtwebkit4 libqt4-test`   
`sudo pip install opencv-contrib-python`   

# GPIO control
With GPIO pins, two different numerations can be used: BOARD (with the numerical position for each pin),
and BCM, the special numeration of broadcom. But this last form is not the same for every raspberry model.  

When program finish, using a keyboard interruption or execution ends, ports used to remain in their last state, and that can be problem. These lines cleans all ports used before. Because of that, don’t use it at the beginning.

<pre>
`def main():`  
    `while True:`  
        `...`
`if __name__ == '__main__':`  
    `try:`
        `main()`  
    `except KeyboardInterrupt:`  
        `...`  
    `finally:`  
        `GPIO.cleanup()`  
</pre>

# Run programs at startup
Run a script with [rc.local](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md) or [cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md).

`sudo nano /etc/rc.local`

At the end of the file, but before the `exit 0`, put the command that must be run during start, with absolute paths:
`python3 /home/pi/example.py &`

If the command runs continuously or is likely not to exit, you must be sure to fork the process by adding an ampersand to the end of the command, `&`. Otherwise, the script will not end and the Pi will not boot. The ampersand allows the command to run in a separate process and continue booting with the process running.


# Remote access

https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0

IP static and SSH https://www.prometec.net/raspberry-pi-ip-estatica/

https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md https://www.raspberrypi.org/documentation/remote-access/ssh/

We have to enable ssh in ifconfigidsf2

Right click on wifi-wire network and open settings We can use GUI programs with -Y

To remove ip host ssh-keygen -R 192.168.3.10

TCPIP https://www.prometec.net/tcpip/ Mascaras https://fireosoft.com.co/blogs/para-que-sirve-la-mascara-de-red/ static IP configuration and access ssh https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md https://www.prometec.net/raspberry-pi-ip-estatica/ GUI remote access with VNC https://www.prometec.net/rpi-acceso-remoto-grafico/

VNC https://www.prometec.net/rpi-acceso-remoto-grafico/ https://www.raspberrypi.org/documentation/remote-access/vnc/ Don’t use :1 when raspberry uses desktop interface, it will appear a grey screen. Use :2 Compartir ficheros https://www.atareao.es/tutorial/raspberry-pi-primeros-pasos/compartir-archivos-mediante-sftp-y-sshfs/ we can drag a folder of pi on the terminal to know the path and use cd.

# Watchdog config
SD cards tend to get corrupted easily, for problems with supply during writing commands. Because of that, use the raspberry in [read-only mode](https://learn.adafruit.com/read-only-raspberry-pi/overview). The script includes a reboot for kernel panics, but these are not the only problems that can freeze the raspi. Because of that, activate the [watchdog](https://www.raspberrypi.org/forums/viewtopic.php?p=1303872). The timer limit is 15 s.

`modprobe bcm2835_wdt`  
`echo "bcm2835_wdt" | sudo tee -a /etc/modules`  

`apt-get install watchdog`  
`update-rc.d watchdog defaults`  

`nano /etc/watchdog.conf`  

Uncomment:

`#watchdog-device`  
`#max-load-1`  

Add:

`watchdog-timeout = 15`  

Save, reboot, test by command:

`:(){ :|:& };:`  

# Read only mode config  

Temporary files are stored in RAM rather than on the SD card. Optionally, you can use a jumper or switch to boot the system into normal read/write mode to install new software or data. And, as normal, you still have easy access to the /boot partition if the SD card is mounted on another computer.

* This does not work with the X11 desktop / PIXEL. It's strictly for Raspbian Lite right now. Graphical applications are still possible using SDL, Pygame and so forth, just not X11 at the moment.
* Setting up read-only mode should be the very last step before deploying a project. THIS SEQUENCE IS IRREVERSIBLE. There is no uninstall script. There’s an option to boot into read/write mode, but nothing to back out all these changes.And back up the contents of your SD card first.

## Install and Run

Pi should be booted and on the network… like mentioned above, everything already configured and fully functional (and backed up) before taking this step. 

From a command line prompt:  
    `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/read-only-fs.sh`  
    `sudo bash read-only-fs.sh`  

The [script](https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/issues) will repeat all these stern warnings and make you verify at several steps whether to continue. Along the way you’ll be presented with a few options:

`Enable boot-time read/write jumper? [y/N]`  

This gives you the option to run the system in read/write mode by inserting a jumper across two pins. If you answer yes to this question, you’ll also be asked for a GPIO pin number. When there’s a jumper between this pin and ground, the system will boot into read/write mode and you can make changes (but remember to do a proper shutdown).
Make sure the pin isn’t used by anything else. GPIO21 is easy to remember because it’s right at the end of the header. If you’re using I2S audio though, that requires GPIO21 for its own use, so you’ll want to pick another.  

`Install GPIO-halt utility? [y/N]`  

This installs a utility that initiates a proper shutdown when another GPIO pin is touched to ground. For a read-only system, you probably don’t need this… but if you have the system booted in read/write mode, this provides an option if you can’t log in and run a manual shutdown. This likewise will ask for a GPIO pin number like GPIO16.

You’re Not Finished Yet. Test the modified system to make sure that the system boots and your application runs as intended. Try a pass with the read/write jumper and/or the gpio-halt button, if you’ve enabled either of those options.

# 3G dongle configuration  

First we have to increase max output current through USBs to avoid hubs like in the picture.  

<img src="https://github.com/JaledMC/Learning-Raspi/blob/master/images/usb_pins.jpg" height="200" width="200">
<img src="https://github.com/JaledMC/Learning-Raspi/blob/master/images/diy_hub.jpg" height="200" width="440"> 

Add the following line to the bottom of /boot/config.txt   
`max_usb_current=1`

Now install usb mode switch to change the dongle function  
`apt-get install usb-modeswitch usb-modeswitch-data`

Create /etc/udev/rules.d/70-usb-modeswitch.rules with the following content:   
`ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="12d1", ATTRS{idProduct}=="1f01", RUN+="/usr/sbin/usb_modeswitch -v 0x12d1 -p 0x1f01 -V 0x12d1 -P 0x1405 -J"`  

This line is for Huawei E3372 and E3531 models. Others dongle may need different IDs. Now then raspi should detects a eth connection.  

* lsusb before udev rule:  
`root@raspberrypi:~# lsusb`  
`Bus 001 Device 003: ID 12d1:1f01 Huawei Technologies Co., Ltd.`  
`Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub`  

* lsusb after udev rule:  
`root@raspberrypi:~# lsusb`  
`Bus 001 Device 003: ID 12d1:14dc Huawei Technologies Co., Ltd.`  
`Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub`  

To avoid wifi connections during boot, we have to set down the wlan, editing rc.local:  
`sudo nano /etc/rc.local`  
`sudo ifconfig wlan0 down`  

# Code examples
* [Led blink](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/blinkLed.py)
* [Knight rider](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/knight%20rider.py)
* [Buttons polling](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/button%20polling.py): with a digital read loop
* [Control buttons with events](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/interruptions%20buttons.py): use pin events to handle push buttons
* [Piano button](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/piano%20audio%20files.py): play sound files throught audio jack with pygame libraty. But warning, use .wav files with 16 bits and 128 bps. Other formats can be used throught other linux program with `subprocess`.
Play sounds on RBpi with a piezo hasn’t much sense because the easiest way is use pwm and with it we lose jack audio output. One way is use audio [utils](https://raspberrypi-aa.github.io/session3/audio.html), [2](https://www.olivieraubert.net/vlc/python-ctypes/), [vlc](https://www.instructables.com/id/The-Raspberry-Pi-Arduino-Connection/), or piGame, to play audio files. We can [synthesize midi audio with Sonic pi](https://projects.raspberrypi.org/en/projects/ultrasonic-theremin), or [PyGame midi](http://www.derickdeleon.com/2014/07/midi-based-theremin-using-raspberry-pi.html).
* [Keypad](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/keypad.py): control the classic 3x3 and 4x4 keypads. Only install the library with `sudo pip3 install pad4pi`

* [Arduino analog read](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/arduino%20analog%20read.py): it'ns better to connect an arduino than use a ADC module.
* [Arduino I2C communication](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/arduino%20I2C%20comm.py): remember to enable the IwC and SPI interfaces on the RBpi, and nstall **i2c tools** to know the devices address:
`sudo apt-get install i2c-tools`
Install smbus to use i2c pins and reboot
`apt-get install python-smbs`
* [LCD 2004 I2C](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/LCD%202004%20I2C.py): only install raspberry LCD library:
`sudo pip3 install RPLCD`

* [Raspi ultrasonic sensor library](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/ultrasonic%20simple.py)
* [Ultrasonic sensor](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/Ultrasonic%20sensor.py): For precise measurement better use C. Remember use a resistor divisor for echo pin
* [Ultrasonic sensor with event](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/Ultrasonic%20with%20event.py)

* [Hardware PWM](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/hardware%20pwm.py): There is only two harware PWM channels on the Raspberry pi, that can be access on GPIOs 12, 13, 18 and 19 (32, 33, 12, and 35). 12 and 18 share same setting as 13 and 19. However, this pwms are us for audio, and we loose them with audio play. We can replace it with software pwm, but is less time precise, maybe for leds application only.
* [Servo control](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/servo%20control.py)

* [USB camera display](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/camera_usb.py)
* [Picamera](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/camera.py): enable camera with piconfig and connect the ribbon cable to the camera connector, (not the display connector, you absent minded). The camera preview only works when a monitor is connected to the Pi, so remote access (such as SSH and VNC) will not allow you to see the camera preview.
* [Picamera capture](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/image%20capture.py)
* [Picamera video capture](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/video%20recording.py)
* [Picamera resize](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/picamera%20resize.py)
* [Picamera brightness & contrast](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/brightness%20%26%20contrast.py)
* [Picamera effects](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/camera%20effects.py)
* [Picamera exposure modes](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/camera%20exposure%20modes.py)
* [Picamera white balance](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/camera%20white%20balance.py)
* [Picamera text on video](https://github.com/JaledMC/Learning-Raspi/blob/master/Examples/text%20on%20video.py)

# Cool projects TODO
* [Arcade machine](https://www.youtube.com/watch?v=psWCmLwvWBE)
    https://pimylifeup.com/raspberry-pi-dosbox/

* [Kodi Media Center](https://pimylifeup.com/raspberry-pi-xbmc-media-center/)
* [Kiosk](https://pimylifeup.com/raspberry-pi-kiosk/)
* [Smart Mirror](https://hackaday.io/project/13466-raspberry-pi-smart-mirror)
    https://magicmirror.builders/

* [Robot](https://www.instructables.com/id/Raspberry-Pi-Web-Controlled-Autonomous-Robot/)
* [Weather station](https://projects.raspberrypi.org/en/projects/temperature-log)

* [Web](https://www.instructables.com/id/Simple-and-intuitive-web-interface-for-your-Raspbe/)
* [Web Server](https://pimylifeup.com/raspberry-pi-nginx/)
    https://pimylifeup.com/raspberry-pi-web-server/
    https://pimylifeup.com/raspberry-pi-plex-server/
    https://maker.pro/raspberry-pi/projects/raspberry-pi-web-server

* [TOR access point](https://pimylifeup.com/raspberry-pi-tor-access-point/)
* [VPN](https://pimylifeup.com/raspberry-pi-vpn-access-point/)
* [Pirate radio](https://pimylifeup.com/raspberry-pi-pirate-radio/)

* [Webcam server]()
* [Camera detection]()
* [Time lapse]()

* [Telegram](https://pimylifeup.com/raspberry-pi-telegram-bot/)
* [Cloud](https://pimylifeup.com/raspberry-pi-owncloud/)
* [Twitter Bot](https://pimylifeup.com/raspberry-pi-twitter-bot/)
* [Alexa](https://pimylifeup.com/raspberry-pi-alexa/)
* [Google assistant](https://pimylifeup.com/raspberry-pi-google-assistant/)
    
# References
* [Hackster](https://www.hackster.io/raspberry-pi/projects?sort=trending&page=3)
* [Pimylifeup](https://pimylifeup.com/)
* [pyimagesearch](https://www.pyimagesearch.com/)
* [raspberrypi.org](https://projects.raspberrypi.org/en)
