# Web LED
a flask server that enables visitors on my site to control LEDs at my desk

[how to set up flask with apache](https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php)

[how to set up https with apache on a raspberry pi](https://pimylifeup.com/raspberry-pi-ssl-lets-encrypt/)

in addition to the tutorials there's a few more steps to take:
- enable the i2c interface with the command `sudo raspi-config`, navigating to `Interfacing Options`, and then `I2C`
- give apache access to the i2c pins with the command `adduser -G i2c www-data`
- if you want to enable public access, set up port forwarding on your router to forward incoming port 80 (and port 443 if you're using https) requests to the respective ports on the pi 
- if you want to use https you'll need to buy a domain name (you can get them dirt cheap, i use [porkbun](https://porkbun.com) and have it point to your ip

![img](https://github.com/avelaga/webLed/blob/master/webLed.gif)
