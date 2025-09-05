def extract_movie_id(slug: str) -> str:
	return slug.replace(".html", '').split('_')[-1]