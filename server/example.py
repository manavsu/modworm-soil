from echo_server import EchoServer
import asyncio

async def main():
    server = EchoServer("127.0.0.1", 10002, 1)
    await server.start()

asyncio.run(main())



