# Learning-Raspi
Learning electronic and programming with Raspberry Pi

# Raspberry setup
Setup Format the SD card in FAT32 Download NOOBS, and copy all files in the zip to the SD card. It’s the easiest way to install Ubuntu Mate or Raspbian, but we can use Chromium too. PD: At present, all OS are 32 bits. Put the SD in the RBpi, connect the keyboard, mouse, display and supply. If the RBpi has bluetooth, we can configure it to use a wireless keyboard and mouse from now.

Install arduino IDE Alternatively, open Chrome on your Raspberry Pi, head to magpi.cc/2tPw8ht, and click the Linux ARM link under ‘Download the IDE’. Extract the file to your /opt directory , then open a Terminal and run the install.sh script to install. cd Downloads/ tar -xf arduino-1.8.3-linuxarm.tar.xz sudo mv arduino-1.8.3 /opt sudo /opt/arduino-1.8.3/install.sh

Install opencv

https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0

Password Your username and password are used for numerous things, including SSHing into your Pi from another machine. It is recommended that you change these defaults for security reasons. Username: pi Password: raspberry

To change password, use “sudo passwd” command.

If raspbian freezes, disconnect usbs and HDMi can help. Disconnect supply could corrupt system files. Use ctrl+alt+f1 to switch to kernel, and use sudo reboot. To return to GUI, use ctrl+alt+f7

Read only!

https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/ install i2c tools to know the devices address sudo apt-get install i2c-tools Install smbus to use i2c pins and reboot apt-get install python-smbus

raspberry fan gpios initialization


# GPIO control
Overview
BCM vs BOARD
To use the GPIO pins two different numerations can be used: board(with the numerical position for each pin),
and BCM, the special numeration of broadcom. But this last form is not the same for every raspberry model

GPIO.cleanup()
When program finish, when using a keyboard interruption or normal end, ports used stay in their last state, and that can be dangerous, and the IDE shows a warning.
This method cleans all ports used before. Because of that, don’t use it at the beginning.


Use this template:

def main():
    while True:
        ...
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...
        pass
    finally:
        GPIO.cleanup()


# Run programs at startup
Run a script with rc.local or cron
https://www.raspberrypi.org/documentation/linux/usage/rc-local.md https://www.raspberrypi.org/documentation/linux/usage/cron.md


# Remote access
IP static and SSH https://www.prometec.net/raspberry-pi-ip-estatica/

https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md https://www.raspberrypi.org/documentation/remote-access/ssh/

We have to enable ssh in ifconfigidsf2

Right click on wifi-wire network and open settings We can use GUI programs with -Y

To remove ip host ssh-keygen -R 192.168.3.10

TCPIP https://www.prometec.net/tcpip/ Mascaras https://fireosoft.com.co/blogs/para-que-sirve-la-mascara-de-red/ static IP configuration and access ssh https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md https://www.prometec.net/raspberry-pi-ip-estatica/ GUI remote access with VNC https://www.prometec.net/rpi-acceso-remoto-grafico/

VNC https://www.prometec.net/rpi-acceso-remoto-grafico/ https://www.raspberrypi.org/documentation/remote-access/vnc/ Don’t use :1 when raspberry uses desktop interface, it will appear a grey screen. Use :2 Compartir ficheros https://www.atareao.es/tutorial/raspberry-pi-primeros-pasos/compartir-archivos-mediante-sftp-y-sshfs/ we can drag a folder of pi on the terminal to know the path and use cd.

# Watchdog configuration
watchdog https://www.raspberrypi.org/forums/viewtopic.php?p=1303872

# 3G Dongle


https://www.raspberrypi.org/forums/viewtopic.php?p=1197625 Important, don’t use any static ip. Autoconfiguration

Shutdown wifi at startup

http://www.magdiblog.fr/divers/ssh-connect-back-comment-garder-la-main-sur-un-raspberry-pi-connecte-a-internet-via-un-dongle-3g/ https://raspberrypi.stackexchange.com/questions/32384/ssh-into-raspberry-pi-with-3g-modem-connected https://raspberrypi.stackexchange.com/questions/46191/remote-control-a-raspberry-pi-currently-behind-a-restricted-wifi-network https://raspberrypi.stackexchange.com/questions/34556/how-to-connect-to-the-raspberry-pi-through-3g-dongle https://raspberrypi.stackexchange.com/questions/23803/how-can-i-access-my-pi-that-is-connected-to-a-3g-network-from-the-outside-intern https://www.reddit.com/r/raspberry_pi/comments/3bm7xd/how_to_ssh_into_raspi_using_3g_modem/ https://zieren.de/raspberry-pi/reverse-ssh-through-3gnat/ https://superuser.com/questions/888491/is-it-possbile-to-ssh-in-linux-from-a-3g-usb-stick-from-t-mobile-with-raspberry https://bandaancha.eu/foros/ofrece-movistar-ip-publica-conexion-3g-1727037 https://www.forocoches.com/foro/showthread.php?t=4923975 https://www.adslzone.net/foro/banda-ancha-movil-3g-y-4g.101/ip-publicas.361239/ https://www.matooma.com/es/noticias/las-tarjetas-sim-m2m-la-mejor-opcion-para-conectar-los-dispositivos http://director-it.com/index.php/es/ssoluciones/comunicacion-entre-maquinas/225-elegir-una-tarjeta-sim.html https://www.tendencias21.net/telefonica/Que-es-la-comunicacion-M2M_a801.html https://www.gemalto.com/latam/iot/m2m/soluciones/mim https://www.raspberrypi.org/forums/viewtopic.php?t=22312

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
