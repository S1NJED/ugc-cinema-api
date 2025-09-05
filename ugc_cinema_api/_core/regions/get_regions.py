from bs4 import BeautifulSoup
from ugc_cinema_api._utils.fetch import fetch

class GetRegions:
	def __init__(self):
		url = "https://www.ugc.fr/cinemas.html" 
		self.dom = 0
		self.soup = 0
		self.regions = []

		req = fetch(url, method="GET")
		self.dom = req.text
		self.soup = BeautifulSoup(self.dom, "html.parser")

		anchors = self.soup.select('div[role="tablist"] a')[3:]

		for anchor in anchors:
			self.regions.append({
				"id": anchor.attrs.get("id").split('-')[-1],
				"name": anchor.text.strip()
			})

	
