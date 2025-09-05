import requests
from requests import Response
from ugc_cinema_api.constants import HEADERS
from typing import Literal
from ugc_cinema_api._utils.transform import transform_query_params


def fetch(
	url: str,
	headers: dict = HEADERS,
	query_params: str = None,
	method: str = Literal["GET", "POST"],
	body: dict = None
) -> Response:
	
	if method == "GET":
		return _GET(url, headers, query_params)
	elif method == "POST":
		return _POST(url, body, headers)


def _GET(
	url: str, 
	headers: dict = HEADERS, 
	query_params: dict = None
) -> Response:
	return requests.get(url, headers=headers, params=transform_query_params(query_params))

def _POST(
	url: str,
	body: dict | str,
	headers: dict = HEADERS,
):
	return requests.post(url, headers=headers, data=body)
