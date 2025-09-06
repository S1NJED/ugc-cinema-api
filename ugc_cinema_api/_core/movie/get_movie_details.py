from ugc_cinema_api.constants import BASE_URL
from ugc_cinema_api._utils.fetch import fetch
from ugc_cinema_api._utils.transform import create_url
from ugc_cinema_api._utils.extract import extract_movie_id
from ugc_cinema_api.constants import HEADERS

from bs4 import BeautifulSoup
from urllib.parse import urlencode
import requests
from requests.exceptions import JSONDecodeError


class MoviePage:

	def __init__(self, slug: str):
		self.slug = slug
		self.dom = fetch(create_url(slug), method="GET")
		self.soup = BeautifulSoup(self.dom.text, "html.parser")
		self.rating_soup = self._init_rating_soup()
		self.trailer = self._fetch_trailer()
		self.duration = None
		self.genres = []
		self.director = None
		self.release_date = None
		self.actors = []
		self.description = None

		self._extract_movie_informations()

	def _get_id(self) -> str:
		return extract_movie_id(self.slug)

	def _get_poster(self) -> str:
		img = self.soup.select_one("section#film-presentation a[data-toggle] img")
		if not img:
			return None
		return img.attrs.get("src")

	def _get_weeks(self) -> str:
		div = self.soup.select_one("div.nb-week")
		if not div:
			return None
		return div.text.strip()

	def _get_title(self) -> str:
		h1 = self.soup.select_one("div.main h1.block--title")
		if not h1:
			return None
		return h1.text.strip()
	
	# todo put this in another class
	def _init_rating_soup(self):
		url = "https://www.ugc.fr/filmRatingAction!displayModal.action"
		data = {
			"filmId": self._get_id(),
			"filmTitle": self._get_title()
		}
		headers = HEADERS
		headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
		headers["Content-Length"] = str(len(urlencode(data)))
		req = fetch(url, headers, body=urlencode(data), method="POST")
		return BeautifulSoup(req.text, "html.parser")
	
	def _get_rating(self) -> str:
		div = self.rating_soup.select_one("div.rating")
		if not div:
			return None
		return div.text.strip()

	def _get_ratings_count(self) -> int:
		div = self.rating_soup.select_one("div.nb-votes")
		if not div:
			return None
		return int(div.text.strip().split()[0])

	def _get_label(self) -> str:
		span = self.soup.select_one("section#film-presentation div.info-wrapper span.film-tag")
		if not span:
			return None
		return span.text.strip()

	# Todo metre dans un autr file
	def _fetch_trailer(self) -> str:
		url = f"https://www.ugc.fr/filmTrailerAjaxAction?"
		params = {
			"filmId": self._get_id()
		}
		req = fetch(url, method="GET",headers={}, query_params=params)
		print(req)
		try:
			data = req.json()
			print(data)
			return data['videos'][0]['src']
		except JSONDecodeError as err:
			return None
		
	def _get_trailer(self) -> str:
		return self.trailer


	# one fn because several info in same str
	def _extract_movie_informations(self):
		elems = self.soup.select("div.group-info p.color--dark-blue")
		info = [elem for elem in elems[0].text.replace('\t', '').split('\n') if len(elem) > 1]
		print(info)
		self.genres = info[0].split(', ')
		self.duration = info[1].strip()
		self.release_date = info[2].removeprefix("Sortie le ")
		self.director = info[3].removeprefix("De ")
		self.actors = info[4].removeprefix("Avec ").split(', ')


	def _get_genres(self) -> list:
		return self.genres

	def _get_duration(self) -> str:
		return self.duration

	def _get_release_date(self) -> str:
		return self.release_date

	def _get_director(self) -> str:
		return self.director

	def _get_actors(self) -> list:
		return self.actors	
