from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import client

logging.basicConfig()
log = logging.getLogger("FlaskAPI")
log.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/echo/<string>", methods=["GET"])
def echo(string):
    log.info(f"Echo {string}")
    return string

@app.route("read_registers/<ip>/<port>/<fc>/<address>/<cnt>", methods=["GET"])
@app.route("read_registers/<ip>/<port>/<fc>/<address>/<cnt>/<slave_id>", methods=["GET"])
def read_registers(ip, port, fc, address, slave_id=None):
    if slave_id:
        return client.read_registers(ip, port, fc, address, 1, slave_id)
    return client.read_registers(ip, port, fc, address, 1)

