from ugc_cinema_api.constants import BASE_URL

def transform_query_params(query_params: str = None) -> str | None:
	if not query_params:
		return None
	return '&'.join( [f"{k}={v}" for k,v in query_params.items()] )

def create_url(endpoint: str):
	return BASE_URL + endpoint
