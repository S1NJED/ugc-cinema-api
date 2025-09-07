from ugc_cinema_api._core.regions.get_regions import *
from ugc_cinema_api._core.cinema.get_cinemas_from_region import *
from ugc_cinema_api.types import Region
import json


class Regions:

	def __init__(self):
		self.regions = self.get_regions()
	
	def __repr__(self):
		return json.dumps(self.regions, indent=4)

	def get_regions(self) -> list[Region]: return GetRegions().regions