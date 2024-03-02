# Package imports 
import RPi.GPIO as GPIO
import flask, json
from flask import render_template, redirect

# File imports
import GPIO_interface

# Start app
app = flask.Flask(__name__)

# functions
def to_default():
    data = {
        "BEAM": [0,400]
    }
    with open('data.json', 'w') as file:
        file.write(json.dumps(data, indent=4))


# Routes 
@app.route("/reset", methods = ['GET'])
def reset():
    if flask.request.method == "GET":
        to_default()
    return redirect("/")

@app.route("/data", methods = ['GET'])
def get_data():
    f = open('data.json')
    data = json.load(f)
    return data


@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    to_default()
    
    # THE ONLY PURPOSE of GPIO_interface.GPIO_Iface is to monitor GPIO pins
    # and edit data in data.json which should be consistant with the formating
    # in the data variable initiated within the to_default function 
    # GPIO_interface.GPIO_Iface is independent of all other functionality
    GPIO.setmode(GPIO.BCM) # Set GPIO mode 
    interface = GPIO_interface.GPIO_Iface(GPIO) # Initialize GPIO_Interface
    app.run(host="0.0.0.0", port=1234, debug=True)