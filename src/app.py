# Package imports 
import RPi.GPIO as GPIO
import flask, json
from flask import render_template

# File imports
import GPIO_interface

# Start app
app = flask.Flask(__name__)

# Routes 
@app.route("/reset", methods = ['POST'])
def reset():
    pass

@app.route("/data", methods = ['GET'])
def get_data():
    f = open('data.json')
    data = json.load(f)
    return data


@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    ran = False
    if not ran:
        GPIO = 3
        interface = GPIO_interface.GPIO_Iface(GPIO)
        #interface.break_beam_callback()
        ran = True
    app.run(host="0.0.0.0", port=1234, debug=False)