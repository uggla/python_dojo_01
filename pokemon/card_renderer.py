import pokemon

from typing import Protocol


class CardRenderer(Protocol):
    def render(
        self, cards: list["pokemon.Pokemon"]
    ) -> str: ...  # pragma: no cover


class TxtCardRenderer:
    def render(self, cards: list["pokemon.Pokemon"]) -> str:
        s = ""
        for i, card in enumerate(cards):
            evolution = _get_evolution_name(card)
            s += (
                f"Fiche Pokemon {i + 1}:\n"
                + f"Name: {card.name}\n"
                + f"Type: {card.type.value}\n"
                + f"Atk: {card.atk}\n"
                + f"Evolution: {evolution}\n"
                + f"Img: {card.img}\n\n"
            )
        return s


class HtmlCardRenderer:
    def render(self, cards: list["pokemon.Pokemon"]) -> str:
        s = ""
        for i, card in enumerate(cards):
            evolution = _get_evolution_name(card)
            s += (
                '<!DOCTYPE html>\n<html lang="en">\n'
                + '<head>\n<meta charset="utf-8">\n'
                + "<title>HTML5 Example Page</title>\n"
                + '<meta name="viewport" '
                + 'content="width=device-width, initial-scale=1">\n'
                + '<meta name="description" content="Pokemon cards">'
                + "</head><body>\n"
                + f"<h1>Fiche Pokemon {i + 1}:</h1>\n"
                + "<ul>\n"
                + f"<li>Name: {card.name}</li>\n"
                + f"<li>Type: {card.type.value}</li>\n"
                + f"<li>Atk: {card.atk}</li>\n"
                + f"<li>Evolution: {evolution}</li>\n"
                + f'<li>Img: <img alt="pokemon" src="{card.img}"></li>\n'
                + "</ul>\n"
                + "</body></html>\n\n"
            )
        return s


def _get_evolution_name(card: "pokemon.Pokemon") -> str:
    evolution = card.evolve()
    if evolution is not None:
        return evolution.name
    return "Pas d'évolution"
