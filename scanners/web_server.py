from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import server_scanner
import network_scanner
import asyncio
from garbage_checker import *

logging.basicConfig()
log = logging.getLogger("FlaskAPI")
log.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/echo/<string>", methods=["GET"])
def echo(string):
    return string

@app.route("/nmap/<ip>", methods=["GET"])
@app.route("/nmap/<ip>/<port>", methods=["GET"])
def scan_network(ip, port='502'):
    ip = ip.replace('+', '/')
    validate_ip(ip) #TODO: change to validate_cidr
    validate_port(port)
    return jsonify(network_scanner.scan_network(ip, port))

@app.route("/smap/<ip>/<port>", methods=["GET"])
@app.route("/smap/<ip>/<port>/<slave_id>", methods=["GET"])
def scan_server(ip, port,slave_id=0):
    validate_ip(ip)
    validate_port(port)
    validate_slave_id(slave_id)
    return jsonify(asyncio.run(server_scanner.scan_server(ip, port, slave_id)))

@app.route("/rregs/<ip>/<port>/<func_code>/<address>/<count>/", methods=["GET"])
@app.route("/rregs/<ip>/<port>/<func_code>/<address>/<count>/<slave_id>/", methods=["GET"])
def read_registers(ip, port, func_code, address, count, slave_id=0):
    validate_ip(ip)
    validate_port(port)
    validate_func_code(func_code)
    address, count = validate_modbus_address(address, count)
    slave_id = validate_slave_id(slave_id)
    return jsonify(asyncio.run(server_scanner.read_registers(ip, port, func_code, address, count, slave_id)))

if __name__ == '__main__':
    app.run(debug=True)

