# Package imports 
import flask, json, threading
from flask import render_template, redirect 

# File imports
import Sensor_Iface

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
    flask.g.title="Sweet P.O.T.A.T.O"
    return render_template("index.html")


if __name__ == "__main__":
    # Start interface in a separate thread
    interface_thread = threading.Thread(target=Sensor_Iface.Sensor_Iface)
    interface_thread.start()
    # Start Flask app
    app.run(host="0.0.0.0", port=1234, debug=True)
