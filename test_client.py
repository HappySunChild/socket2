from websockets import WebSocketClientProtocol
from socket2 import WebsocketClient

class MyClient(WebsocketClient):
	async def on_connect(self, socket: WebSocketClientProtocol):
		print(socket)

client = MyClient('ws://localhost:8080')
client.connect()