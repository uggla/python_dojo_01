import pokemon
import random

from pokemon import exception
from pokemon import card_renderer
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


class PlayerView:
    def __init__(
        self, player: Player, card_renderer: card_renderer.CardRenderer
    ) -> None:
        self.player = player
        self.renderer = card_renderer

    def show_cards(self) -> str:
        return self.renderer.render(self.player.cards)
