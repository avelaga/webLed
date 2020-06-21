# Web LED
a flask server that enables visitors on my site to control LEDs at my desk

[how to set up flask with apache](https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php)

[how to set up https with apache on a raspberry pi](https://pimylifeup.com/raspberry-pi-ssl-lets-encrypt/)

in addition to the tutorials there's a few more steps to take:
- give apache access to the i2c pins with the command `adduser -G i2c www-data`

![img](https://github.com/avelaga/webLed/blob/master/webLed.gif)
