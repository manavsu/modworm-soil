from pymodbus.client import AsyncModbusTcpClient
import logging
import asyncio
from pymodbus.mei_message import ReadDeviceInformationResponse
from pymodbus.constants import DeviceInformation


logging.basicConfig()
log = logging.getLogger("FlaskClient")

async def scan_server(ip, port, slave_id=0):
    log.debug(f"scan_server {ip}:{port} id={slave_id}")
    client = AsyncModbusTcpClient(ip, port)
    await client.connect()  # Using 0x0E for basic device identification
    result:ReadDeviceInformationResponse = await client.read_device_information(read_code=DeviceInformation.EXTENDED, object_id=slave_id)
    client.close()
    if result.isError():
        log.warning(f"scan_server {ip}:{port} id={slave_id} -> {result}")
    print(result.information)
    return result

asyncio.run(scan_server("127.0.0.1", 10002))