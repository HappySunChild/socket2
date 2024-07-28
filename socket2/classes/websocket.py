from websockets import connect, WebSocketClientProtocol, ConnectionClosed
from json import dumps

from .response import WebsocketResponse

class WebsocketClient:
	def __init__(self, uri: str) -> None:
		self.connected = False
		
		self.uri = uri
		self.socket: WebSocketClientProtocol = None
	
	async def connect(self):
		self.connected = True
		self.socket = await connect(uri=self.uri)
	
	async def send(self, data):
		if not self.connected:
			return
		
		await self.socket.send(dumps(data))
	
	async def receive(self) -> WebsocketResponse:
		if not self.connected:
			return
		
		data = None
		ok = True
		
		try:
			data = await self.socket.recv()
		except ConnectionClosed:
			ok = False
		
		return WebsocketResponse(message=data, ok=ok)