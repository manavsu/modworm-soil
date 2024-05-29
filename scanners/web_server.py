from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import server_scanner
import network_scanner
import asyncio
from garbage_checker import *
from time import sleep

logging.basicConfig()
log = logging.getLogger("FlaskAPI")
log.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def validate(func_msg_pairs):
    for func, fail_msg in func_msg_pairs:
        if not func():
            return jsonify({"error": fail_msg}), 400

@app.route("/echo/<string>/", methods=["GET"])
def echo(string):
    return string

@app.route("/nmap/<ip>/", methods=["GET"])
@app.route("/nmap/<ip>/<port>/", methods=["GET"])
def scan_network(ip, port='502'):
    ip = ip.replace('+', '/')
    bad_request = validate(
        [
            (lambda: validate_ip(ip), "Invalid IP address"),
            (lambda: validate_port(port), "Invalid port number")
        ]
    )
    if bad_request:
        log.error(f"{scan_network.__name__} {bad_request[1]} : {bad_request[0].json["error"]}")
        return bad_request
    return jsonify(network_scanner.scan_network(ip, port))

@app.route("/mmap/<ip>/<port>/", methods=["GET"])
@app.route("/mmap/<ip>/<port>/<slave_id>/", methods=["GET"])
def scan_server(ip, port,slave_id=0):
    bad_request = validate(
        [
            (lambda: validate_ip(ip), "Invalid IP address"),
            (lambda: validate_port(port), "Invalid port number"),
            (lambda: validate_slave_id(slave_id), "Invalid slave ID")
        ]
    )
    if bad_request:
        log.error(f"{scan_server.__name__} {bad_request[1]} : {bad_request[0].json["error"]}")
        return bad_request
    return jsonify(asyncio.run(server_scanner.scan_server(ip, port, slave_id)))

@app.route("/rregs/<ip>/<port>/<func_code>/<address>/<count>/", methods=["GET"])
@app.route("/rregs/<ip>/<port>/<func_code>/<address>/<count>/<slave_id>/", methods=["GET"])
def read_registers(ip, port, func_code, address, count, slave_id=0):
    bad_request = validate(
        [
            (lambda: validate_ip(ip), "Invalid IP address"),
            (lambda: validate_port(port), "Invalid port number"),
            (lambda: validate_func_code(func_code), "Invalid function code"),
            (lambda: validate_modbus_address(address, count), "Invalid address or count"),
            (lambda: validate_slave_id(slave_id), "Invalid slave ID")
        ]
    )
    if bad_request:
        log.error(f"{read_registers.__name__} {bad_request[1]} : {bad_request[0].json["error"]}")
        return bad_request
    return jsonify(asyncio.run(server_scanner.read_registers(ip, port, func_code, address, count, slave_id)))

@app.route("/deviceinfo/<ip>/<port>/", methods=["GET"])
@app.route("/deviceinfo/<ip>/<port>/<slave_id>/", methods=["GET"])
def device_info(ip, port, slave_id=0):
    bad_request = validate(
        [
            (lambda: validate_ip(ip), "Invalid IP address"),
            (lambda: validate_port(port), "Invalid port number"),
            (lambda: validate_slave_id(slave_id), "Invalid slave ID")
        ]
    )
    if bad_request:
        log.error(f"{device_info.__name__} {bad_request[1]} : {bad_request[0].json["error"]}")
        return bad_request
    return jsonify(asyncio.run(server_scanner.read_device_info(ip, port, slave_id)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50901, debug=True)


