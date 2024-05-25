from pymodbus.client import AsyncModbusTcpClient
import logging
import asyncio

logging.basicConfig()
log = logging.getLogger("FlaskClient")


async def read_holding_registers(ip, port, address, count, slave_id=0):
    log.debug(f"read_register {ip}:{port} {address}")
    client = AsyncModbusTcpClient(ip, port)
    await client.connect()
    result = await client.read_holding_registers(address, count, unit=slave_id)
    client.close()
    if result.isError():
        log.warning(f"read_register {ip}:{port} {address}-{count} {slave_id} -> {result}")
        return result
    return result.registers

async def scan_server(ip, port, slave_id=0):
    log.debug(f"scan_server {ip}:{port} id={slave_id}")
    client = AsyncModbusTcpClient(ip, port)
    await client.connect()
    result = await client.read_device_information()
    client.close()
    if result.isError():
        log.warning(f"scan_server {ip}:{port} -> {result}")
        return result
    return result

asyncio.run(read_registers("127.0.0.1", 10002, 1000, 1))