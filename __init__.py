from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from smbus import SMBus
import time

@app.route("/led")
def hue():
	addr = 0x8 # bus address
	bus = SMBus(1)
	bus.write_byte(addr,0)
	time.sleep(1)
	return "toggled led"

if __name__ == '__main__':
    app.run()
