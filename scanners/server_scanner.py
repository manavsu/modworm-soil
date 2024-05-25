from pymodbus.client import AsyncModbusTcpClient
import logging
import asyncio
from pymodbus.mei_message import ReadDeviceInformationResponse
from pymodbus.constants import DeviceInformation
import enum
import time
import concurrent.futures


logging.basicConfig()
log = logging.getLogger("ServerScanner")
log.setLevel(logging.DEBUG)

class Tables(enum.Enum):
    COILS = 0x01
    DISCRETE_INPUTS = 0x02
    HOLDING_REGISTERS = 0x03
    INPUT_REGISTERS = 0x04

class ScanningClient:
    def __init__(self, ip, port, slave_id=0) -> None:
        self.log_prefix = f"scan_client {ip}:{port} id={slave_id}"
        log.debug(f"{self.log_prefix} created")
        self.client = AsyncModbusTcpClient(ip, port)
        self.slave_id = slave_id

    
    async def connect(self):
        await self.client.connect()
    
    def close(self):
        self.client.close()
    
    async def read_device_information(self, read_code=DeviceInformation.EXTENDED):
        result:ReadDeviceInformationResponse = await self.client.read_device_information(read_code=read_code, object_id=self.slave_id)
        if result.isError():
            log.warning(f"{self.log_prefix} read_device_information code={read_code} -> {result}")
        return self.format_device_info(result)

    def __merge(self, range_a, range_b):
        if not range_a or not range_b:
            return range_a + range_b
        if range_a[0][0] + range_a[0][1] == range_b[0][0]:
            return [(range_a[0][0], range_a[0][1] + range_b[0][1])]
        return range_a + range_b
    
    async def binary_scan(self, read_func, address=0x0000, count=0xFFFF):
        '''
        Recursively scans the address range using binary search, better for populated register maps.
        '''

        result = await read_func(address, count, self.slave_id)
        if not result.isError():
                return [(address, count)]
        if count == 1:
            return []
        return self.__merge(await self.binary_scan(read_func, address, count//2), await self.binary_scan(read_func, address + count//2, count//2 + count % 2))
    
    async def linear_scan(self, read_func, address=0x0000, count=0xFFFF):
        '''
        Scans the address range linearly, better for sparsely populated register maps.
        '''

        range_list = []
        i = address
        while i < address + count:
            result = await read_func(address + i, 1, self.slave_id)
            j = 0
            while (not result.isError() and j < address + count):
                j += 1
                result = await read_func(i + j, 1, self.slave_id)
            if j > 0:
                range_list.append((i, j))
                i += j
            i += 1
            
        return range_list

    async def scan_tables_linear(self):
        '''
        Scans all tables linearly.
        '''

        start_time = time.time()
        table = {
            "coils" : await self.linear_scan(self.client.read_coils),
            "discrete_inputs" : await self.linear_scan(self.client.read_discrete_inputs),
            "holding_registers" : await self.linear_scan(self.client.read_holding_registers),
            "input_registers" : await self.linear_scan(self.client.read_input_registers),
        }
        log.debug(f"{self.log_prefix} scan_tables_linear -> scanned in {time.time() - start_time:.2f} seconds")
        return table


    def format_device_info(self, info:ReadDeviceInformationResponse):
        label_map = {
            0x00: "VendorName",
            0x01: "ProductCode",
            0x02: "MajorMinorRevision",
            0x03: "VendorUrl",
            0x04: "ProductName",
            0x05: "ModelName",
            0x06: "UserApplicationName",
            0x07: "reserved",
            0x08: "reserved",   
        }
        return {label_map[key] : str(info.information[key]) for key in info.information}

async def scan_server(ip:str, port:int, slave_id=0):
    results = {}
    scanner = ScanningClient(ip, port, slave_id)
    await scanner.connect()
    results["device_info"] = await scanner.read_device_information()
    results["tables"] = await scanner.scan_tables_linear()
    log.debug(f"scan_server {ip}:{port} id={slave_id} -> {results}")
    scanner.close()
    return results


