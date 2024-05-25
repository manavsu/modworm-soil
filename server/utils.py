from pymodbus.server import ModbusTcpServer
import asyncio
from contextlib import suppress
import logging
import os

logging.basicConfig()
log = logging.getLogger("EchoServer")
log.setLevel(logging.INFO)

class _serverList:
    """Maintains information about the active server.

    :meta private:
    """

    active_server: ModbusTcpServer = None # type: ignore[assignment]

    def __init__(self, server):
        """Register new server."""
        self.server = server
        self.loop = asyncio.get_event_loop()

    @classmethod
    async def run(_, server, custom_functions) -> None:
        """Help starting/stopping server."""
        for func in custom_functions:
            server.decoder.register(func)
        _serverList.active_server = _serverList(server)  # type: ignore[assignment]
        with suppress(asyncio.exceptions.CancelledError):
            await server.serve_forever()

    @classmethod
    async def async_stop(_) -> None:
        """Wait for server stop."""
        if not _serverList.active_server:
            raise RuntimeError("ServerAsyncStop called without server task active.")
        await _serverList.active_server.shutdown()  # type: ignore[union-attr]
        _serverList.active_server = None  # type: ignore[assignment]

    @classmethod
    def stop(_):
        """Wait for server stop."""
        if not _serverList.active_server:
            log.info("ServerStop called without server task active.")
            return
        if not _serverList.active_server.loop.is_running():
            log.info("ServerStop called with loop stopped.")
            return
        future = asyncio.run_coroutine_threadsafe(_serverList.async_stop(), _serverList.active_server.loop)
        future.result(timeout=10 if os.name == 'nt' else 0.1)

def ServerStop():
    """Terminate server."""
    _serverList.stop()

async def StartAsyncTcpServer(  # pylint: disable=invalid-name,dangerous-default-value
    context=None,
    identity=None,
    address=None,
    custom_functions=[],
    **kwargs,
):
    """Start and run a tcp modbus server.

    :param context: The ModbusServerContext datastore
    :param identity: An optional identify structure
    :param address: An optional (interface, port) to bind to.
    :param custom_functions: An optional list of custom function classes
        supported by server instance.
    :param kwargs: The rest
    """
    server = ModbusTcpServer(context, identity, address)
    await _serverList.run(server, custom_functions)