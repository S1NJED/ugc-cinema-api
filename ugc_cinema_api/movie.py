from ugc_cinema_api._core.movie.get_movie_details import MoviePage
import json


# Interface
class Movie:


	def __init__(self, slug: str):
		self.page = MoviePage(slug)

		self.slug = slug
		self.id = self.get_id()
		self.poster = self.get_poster()
		self.title = self.get_title()
		self.label = self.get_label()
		self.rating = self.get_rating()
		self.ratings_count = self.get_ratings_count()
		self.trailer = self.get_trailer()
		self.duration = self.get_duration()
		self.release_date = self.get_release_date()
		self.director = self.get_director()
		self.genres = self.get_genres()
		self.actors = self.get_actors()
		self.weeks = self.get_weeks()

	def __repr__(self):
		attrs = self.__dict__
		del attrs['page']

		return json.dumps(attrs, indent=4)

	def get_id(self) -> str: return self.page._get_id()
	def get_poster(self) -> str: return self.page._get_poster()
	def get_weeks(self) -> str: return self.page._get_weeks()
	def get_title(self) -> str: return self.page._get_title()
	def get_rating(self) -> str: return self.page._get_rating()
	def get_ratings_count(self) -> int: return self.page._get_ratings_count()
	def get_label(self) -> str: return self.page._get_label()
	def get_trailer(self) -> str: return self.page._get_trailer()
	def get_genres(self) -> list: return self.page._get_genres()
	def get_duration(self) -> str: return self.page._get_duration()
	def get_release_date(self) -> str: return self.page._get_release_date()
	def get_director(self) -> str: return self.page._get_director()
	def get_actors(self) -> list: return self.page._get_actors()
	
