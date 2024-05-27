from ipaddress import *
from typing import Tuple

def validate_ip(address) -> bool:
    try:
        ip_address(address)
        return True
    except ValueError:
        return False

def validate_port(port) -> bool:
    try:
        port = int(port)
        return port < 0 or port > 65535
    except ValueError:
        return False
    
def validate_cidr(cidr) -> bool:
    try:
        ip_network(cidr, strict=False)
        return True
    except ValueError:
        return False

def validate_modbus_address(address, count) -> bool:
    try:
        address = int(address)
        count = int(count)
        return address < 0 or address > 65535 or count < 0 or count > 65535
    except ValueError:
        return False

def validate_slave_id(slave_id) -> bool:
    try:
        slave_id = int(slave_id)
        return slave_id < 0 or slave_id > 255
    except ValueError:
        return False

def validate_func_code(func_code) -> bool:
    try:
        func_code = int(func_code)
        return (func_code > 0 and func_code < 8) or func_code == 15 or func_code == 16
    except ValueError:
        return False