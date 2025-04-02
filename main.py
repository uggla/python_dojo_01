import pokemon
from pokemon import card_renderer


def main():
    player = pokemon.Player()
    player.pick()
    player.pick()
    viewer = pokemon.PlayerView(player, card_renderer.HtmlCardRenderer())
    s = viewer.show_cards()
    print(s)


if __name__ == "__main__":  # pragma: no cover
    main()
