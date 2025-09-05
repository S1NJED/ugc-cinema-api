from dataclasses import dataclass
from pydantic import BaseModel

class Cinema(BaseModel):
	# region_id: str
	cinema_id: str
	name: str
	movie_count: int
	preview_count: int
	address: str

class Region(BaseModel):
	id: str
	name: str

class Movie(BaseModel):
	pass

class Seance(BaseModel):
	pass
