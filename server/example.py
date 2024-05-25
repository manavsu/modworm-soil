from echo_server import EchoServer
import asyncio

server = EchoServer("127.0.0.1", 10003, 1)
server.start()
input("Press Enter to stop the server\n")
server.stop()
