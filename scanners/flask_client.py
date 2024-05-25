from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import server_scanner
import network_scanner
import asyncio

logging.basicConfig()
log = logging.getLogger("FlaskAPI")
log.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/echo/<string>", methods=["GET"])
def echo(string):
    return string

@app.route("/scan_server/<ip>/<port>", methods=["GET"])
@app.route("/scan_server/<ip>/<port>/<slave_id>", methods=["GET"])
def scan_server(ip, port,slave_id=0):
    return jsonify(asyncio.run(server_scanner.scan_server(ip, port, slave_id)))

@app.route("/scan_network/<ip>", methods=["GET"])
@app.route("/scan_network/<ip>/<port>", methods=["GET"])
def scan_network(ip, port='502'):
    return jsonify(network_scanner.scan_network(ip, port))

if __name__ == '__main__':
    app.run(debug=True)

