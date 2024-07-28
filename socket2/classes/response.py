from json import loads

class WebsocketResponse:
	def __init__(self, message: str, ok: bool = True) -> None:
		self.message = message
		self.ok = ok
	
	@property
	def json(self):
		try:
			return loads(self.message)
		except:
			return None
	
	def __repr__(self) -> str:
		return f'<{self.__class__.__name__}: {self.message!r}>'