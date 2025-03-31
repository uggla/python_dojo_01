import pokemon
import random

from pokemon import exception
from pokemon.ext_api import tyradex


class Player:
    MAX_POINTS: int = 3

    def __init__(self) -> None:
        self.cards: list[pokemon.Pokemon] = []
        self.points: int = self.MAX_POINTS

    def pick(self):
        if self.points == 0:
            raise exception.CannotPickMore

        cards = tyradex.get_pokemons()
        # Warning the first card is a header so we need to skip it
        card = random.choice(cards[1:])

        self.points -= 1
        card = pokemon.Pokemon.from_dict(card)
        self.cards.append(card)
