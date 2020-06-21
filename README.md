# Web LED
a flask server that enables visitors on [my site](https://abhi.work/hi) to control LEDs at my desk

![img](https://github.com/avelaga/webLed/blob/master/webLed.gif)

[how to set up flask with apache](https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php)

[how to set up https with apache on a raspberry pi](https://pimylifeup.com/raspberry-pi-ssl-lets-encrypt/)

in addition to the tutorials there's a few more steps to take:
- enable the i2c interface with the command `sudo raspi-config`, navigating to `Interfacing Options`, and then `I2C`
- give apache access to the i2c pins with the command `sudo adduser www-data i2c`
- if you want to enable public access, set up port forwarding on your router to forward incoming port 80 (and port 443 if you're using https) requests to the respective ports on the pi 
- if you want to use https you'll first need to buy a domain name (you can get them dirt cheap, i use [porkbun](https://porkbun.com)) and have it point to your ip
- i had problems with pip3 not installing flask-cors in the expected directory so i had to run `sudo pip3 install -t /usr/lib/python3/dist-packages/ flask-cors` to force it to install in the correct location

my rpi tells an arduino nano over the i2c connection to run the animation. you don't have to use an arduino, i chose to so that i could use the FastLED library that's available for it. if you want to control them directly from the rpi you'll want to use [neopixel](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage) and additionally give the apache user gpio permissions with `sudo adduser www-data gpio'.
