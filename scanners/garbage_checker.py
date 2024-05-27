from ipaddress import *
from typing import Tuple

def validate_ip(address) -> IPv4Address | IPv6Address:
    try:
        return ip_address(address)
    except ValueError:
        raise ValueError("Invalid IP address")

def validate_port(port) -> int:
    try:
        port = int(port)
        if port < 0 or port > 65535:
            raise ValueError("Invalid port number")
        return port
    except ValueError:
        raise ValueError("Invalid port number")
    
def validate_cidr(cidr) -> IPv4Network | IPv6Network:
    try:
        return ip_network(cidr, strict=False)
    except ValueError:
        raise ValueError("Invalid CIDR")

def validate_modbus_address(address, count) -> Tuple[int, int]:
    try:
        address = int(address)
        count = int(count)
        if address < 0 or address > 65535 or count < 0 or count > 65535:
            raise ValueError("Invalid Modbus address or count")
        return address, count
    except ValueError:
        raise ValueError("Invalid Modbus address or count")

def validate_slave_id(slave_id) -> int:
    try:
        slave_id = int(slave_id)
        if slave_id < 0 or slave_id > 255:
            raise ValueError("Invalid Modbus slave ID")
        return slave_id
    except ValueError:
        raise ValueError("Invalid Modbus slave ID")

def validate_func_code(func_code) -> int:
    try:
        func_code = int(func_code)
        if (func_code > 0 and func_code < 8) or func_code == 15 or func_code == 16:
            return func_code
        raise ValueError("Invalid Modbus function code")
    except ValueError:
        raise ValueError("Invalid Modbus function code")