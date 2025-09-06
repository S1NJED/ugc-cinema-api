from ugc_cinema_api._utils.fetch import fetch
from bs4 import BeautifulSoup


def getCinemaFromRegion(regionId: str):
	cinemas = []
	
	url = f"https://www.ugc.fr/cinemasAjaxAction!getCinemasList.action?id={regionId}"
	req = fetch(url, method="GET")
	soup = BeautifulSoup(req.text, "html.parser")

	scrapped_cinemas = [cinema for cinema in soup.select("div.band") if not "cinema-empty" in cinema.attrs['class']]

	for cinema in scrapped_cinemas:
		base_path = "div > div > div > div > "
		obj = {
			"id": cinema.select_one(base_path + "div > ul > li").attrs.get("data-distance-id"),
			"name": cinema.select_one(base_path + "a").attrs.get("title"),
			"movieAmount": cinema.select_one(base_path + "div > p:nth-of-type(1)").text, # useless for now jsp qd je vais l'add mais on verra
			"address": cinema.select_one(base_path + "div > p:nth-of-type(2)").text
		}

		cinemas.append(obj)
	return cinemas