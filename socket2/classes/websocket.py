from typing import Callable

from websockets import connect, serve, WebSocketClientProtocol, WebSocketServerProtocol, ConnectionClosed
from json import dumps
from asyncio import run, Future

from .response import WebsocketResponse

class WebsocketClient:
	def __init__(self, uri: str) -> None:
		self.is_connected = False
		
		self.uri = uri
		self.socket: WebSocketClientProtocol = None
	
	async def on_connect(self, socket: WebSocketClientProtocol):
		pass
	
	async def send(self, data):
		if not self.is_connected:
			return
		
		await self.socket.send(dumps(data))
	
	async def receive(self) -> WebsocketResponse:
		if not self.is_connected:
			return
		
		data = None
		ok = True
		
		try:
			data = await self.socket.recv()
		except ConnectionClosed:
			ok = False
		
		return WebsocketResponse(message=data, ok=ok)
	
	async def _connect(self):
		self.is_connected = True
		self.socket = await connect(uri=self.uri)
		
		await self.on_connect(socket=self.socket)
	
	def connect(self):
		run(self._connect())

class WebsocketServer:
	def __init__(self, host: str, port: int) -> None:
		self.host = host
		self.port = port
	
	async def handler(self, websocket: WebSocketServerProtocol):
		pass
	
	async def on_serve(self):
		pass
	
	async def _serve_handler(self, websocket: WebSocketServerProtocol):
		await self.handler(websocket=websocket)
	
	async def _serve(self, **kwargs):
		await self.on_serve()
		
		async with serve(ws_handler=self._serve_handler, host=self.host, port=self.port, **kwargs):
			await Future()
	
	def serve(self, **kwargs):
		run(self._serve(**kwargs))