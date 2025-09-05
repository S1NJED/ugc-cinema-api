from ugc_cinema_api._utils.fetch import fetch
from bs4 import BeautifulSoup
from ugc_cinema_api.types import Cinema

def _get_cinemas(regionId: str) -> list[Cinema]:		
	cinemas = []
	url = f"https://www.ugc.fr/cinemasAjaxAction!getCinemasList.action?id={regionId}"
	req = fetch(url, method="GET")
	soup = BeautifulSoup(req.text, "html.parser")

	scrapped_cinemas = [cinema for cinema in soup.select("div.band") if not "cinema-empty" in cinema.attrs['class']]

	for cinema in scrapped_cinemas:
		base_path = "div > div > div > div > "
		count_div = cinema.select_one(base_path + "div > p:nth-of-type(1)").text.replace('\n', '').strip().split('|')
		movie_count = ''.join(char for char in count_div[0] if char.isdigit())
		preview_count = 0
		if len(count_div) == 2:
			preview_count = ''.join(char for char in count_div[1] if char.isdigit())

		obj = {
			"cinema_id": cinema.select_one(base_path + "div > ul > li").attrs.get("data-distance-id"),
			"name": cinema.select_one(base_path + "a").attrs.get("title"),
			"movie_count": int(movie_count),
			"preview_count": int(preview_count),
			"address": cinema.select_one(base_path + "div > p:nth-of-type(2)").text
		}

		cinemas.append(Cinema(**obj))
	return cinemas