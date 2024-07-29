from websockets import WebSocketServerProtocol
from socket2 import WebsocketServer

class MyServer(WebsocketServer):
	async def handler(self, websocket: WebSocketServerProtocol):
		print(websocket)
	
	async def on_serve(self):
		print('server websocket started')

server = MyServer('localhost', 8080)
server.serve()