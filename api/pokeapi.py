# In a real project, I'd probably use the Python pokeapi wrapper,
# https://github.com/GregHilmes/pokebase, b/c it's more tested, stable, and complete.
# But that would trivialize this, so I wrote my own API wrapper.

import requests

# Using 3.6 backport
# noinspection PyCompatibility
from dataclasses import dataclass
from requests import Response


@dataclass
class Pokemon:
    id: int
    name: str


def fetch_pokemon(id_or_name: str) -> Pokemon:
    response: Response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_or_name}/")
    # id and name will already be fields in JSON, so use them as kwargs directly
    json = response.json()
    return Pokemon(id=json["id"], name=json["name"])
