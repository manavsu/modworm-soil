
import asyncio
import logging

from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusSlaveContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server import StartAsyncTcpServer, ServerStop


VERSION = "1.0.0"

# Used to map the function code to the data block
OUTPUT_COILS = 0x01
INPUT_CONTACTS = 0x02
HOLDING_REGISTERS = 0x03
INPUT_REGISTERS = 0x04
        

logging.basicConfig()
_logger = logging.getLogger("EchoServer")
_logger.setLevel(logging.INFO)


class EchoServer:
    """
    A simple echo server for testing.

    Discrete Output Coils
    Addr:0 (0x0000) -> toggled continuously
    Addr:1-1000 (0x0000-0x03E7) -> echoed to Addr:1001-2000 (0x03E8-0x07D0)
    
    Analog Output Holding Registers
    Addr:0 (0x0000) -> incremented continuously
    Addr:1-1000 (0x0000-0x03E7) -> echoed to Addr:1001-2000 (0x03E8-0x07D0)

    Discrete Input Contacts (Readonly)
    Addr:0 (0x0000) -> toggled continuously
    Addr:1-1000 (0x0000-0x03E7) -> echoed from Discrete Output Coils Addr:1-1000 (0x03E8-0x07D0)

    Analog Input Registers (Readonly)
    Addr:0 (0x0000) -> incremented continuously
    Addr:1-1000 (0x0000-0x03E7) -> echoed from Analog Output Holding Registers Addr:1-1000 (0x03E8-0x07D0)
    """

    def __init__(self, host:str, port:int, num_clients:int, interval_seconds:int=1):
        self.interval_seconds = interval_seconds
        self.echo_task = None
        create_datablock = lambda cnt : ModbusSequentialDataBlock(0x0000, [0x00] * cnt)
        self.context = {}
        for i in range(num_clients):
            self.context[i] = ModbusSlaveContext(
                di=create_datablock(1000),
                co=create_datablock(2000),
                hr=create_datablock(2000),
                ir=create_datablock(1000),
            )
        identity = ModbusDeviceIdentification(
            info_name={
                "VendorName": "Modworm",
                "ProductCode": "ES",
                "VendorUrl": "https://modworm.com",
                "ProductName": "Echo Server",
                "MajorMinorRevision": VERSION,
            })
        
        StartAsyncTcpServer(self.context, identity, (host, port))
        _logger.info(f"Echo server listening on {host}:{port}")
    
    def start(self):
        self.echo_task = asyncio.create_task(self.__start())
    
    async def __start(self):
        _logger.info("Starting echo function")
        try:
            while True:
                for slave in self.context.values():
                    slave: ModbusSlaveContext

                    slave.setValues(OUTPUT_COILS, 0, [slave.getValues(OUTPUT_COILS, 0, 1)[0] ^ 0x01])
                    slave.setValues(INPUT_CONTACTS, 0, slave.getValues(OUTPUT_COILS, 0, 1))
                    slave.setValues(HOLDING_REGISTERS, 0, [slave.getValues(HOLDING_REGISTERS, 0, 1)[0] + 1])
                    slave.setValues(INPUT_REGISTERS, 0, slave.getValues(HOLDING_REGISTERS, 0, 1))

                    values = slave.getValues(HOLDING_REGISTERS, 1, 999)
                    slave.setValues(HOLDING_REGISTERS, 1000, values)
                    slave.setValues(INPUT_REGISTERS, 1, values)

                    values = slave.getValues(OUTPUT_COILS, 1, 999)
                    slave.setValues(OUTPUT_COILS, 1000, values)
                    slave.setValues(INPUT_CONTACTS, 1, values)
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            return

    def stop(self):
        _logger.info("Stopping echo function")
        self.echo_task.cancel()
        ServerStop()