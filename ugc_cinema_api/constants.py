from random import choice

USER_AGENTS = [
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
]

HEADERS = {
	"User-Agent": choice(USER_AGENTS)
}

BASE_URL = "https://www.ugc.fr/"
