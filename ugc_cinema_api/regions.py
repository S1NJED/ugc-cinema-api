from ugc_cinema_api._core.regions.get_regions import *
import json


class Regions:

	def __init__(self):
		self.regions = GetRegions().regions
	
	def __repr__(self):
		return json.dumps(self.regions, indent=4)
