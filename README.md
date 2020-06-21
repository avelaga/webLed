# Flask backend for my room leds
To run:
- Install the dependencies with the command, `pip install -r requirements.txt`
- From the root of the repo, run `export FLASK_APP=api.py` to set the file that flask will direct to
- Run `flask run -h 0.0.0.0 -p 8000` to start the server

The server will now be running at <ip/hostname>:8000 on the local network.

The hue endpoint takes a required parameter, hue, that must be an int.
You can do this by accessing the get endpoint with this syntax - '/hue?hue=<:number>'
### To deploy
Ideally you [connect an http server like apache to the server](https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/) but since I'm having issues getting it working I'm temporarily having it run the dev server at startup
### To start at boot with the use of screen: (not ideal)
- Install screen with `sudo apt-get install screen`
- Go into the repo and run `chmod +x ~/startup` to give the startup script execution permissions
- Run `sudo nano /etc/rc.local` to edit a file that runs at boot and add `sudo su - pi -c "screen -dm -S api ~/room-led-api/startup"` at the end right before `exit 0`. This starts a detached screen named api and then runs the script startup in it.
- Run `sudo reboot` and see if the api works at the expected url when it's back up. To verify if the screen was created properly, ssh in and run `screen -list` to see all screens. You should see one titled pistartup which you can go into with the command `screen -r api`

## UI and Arduino Controller Repos:
[React UI running on a Raspberry Pi 4 to control the LEDs](https://github.com/avelaga/room-led-ui)

[Arduino code that controls the LEDs](https://github.com/avelaga/room-led-controller)

![img](https://github.com/avelaga/room-led-controller/blob/master/example.gif)
