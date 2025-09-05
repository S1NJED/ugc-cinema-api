from ugc_cinema_api._core.region import _get_cinemas
from ugc_cinema_api.types import Cinema

class Region:
	def __init__(self, regionId: str):
		self.regionId = regionId
	
	def get_cinemas(self) -> list[Cinema]: return _get_cinemas(self.regionId)
