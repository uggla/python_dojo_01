import requests

from functools import cache
from pokemon import exception

URL: str = "https://tyradex.vercel.app/api/v1/pokemon"


@cache
def get_pokemons() -> list[dict[str, object]]:
    try:
        output = requests.get(URL).json()
    except requests.exceptions.RequestException:
        raise exception.ConnectionError("Cannot connect to external API")
    return output
