import json


def fake_pokemons():
    with open("pokemon/tests/fake_pokemons.json", "r") as f:
        return json.loads(f.read())


class Response:
    def __init__(self, data: str) -> None:
        self.data = data

    def json(self):
        return json.loads(self.data)


def fake_requests():
    with open("pokemon/tests/fake_pokemons.json", "r") as f:
        return Response(f.read())
