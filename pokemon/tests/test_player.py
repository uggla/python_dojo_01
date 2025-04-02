import pokemon
import pytest

from pokemon import card_renderer
from pokemon import exception
from pokemon.ext_api import tyradex
from pokemon.tests import fakes


def test_player_instance():
    player = pokemon.Player()
    assert player.cards == []
    assert player.points == 3


def test_player_pick(monkeypatch, mocker):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    mocker.patch(
        "pokemon.player.random.choice", return_value=fakes.fake_pokemons()[1]
    )

    player = pokemon.Player()
    player.pick()
    assert len(player.cards) == 1
    assert player.points == 2
    assert isinstance(player.cards[0], pokemon.Pokemon)
    player.pick()
    assert len(player.cards) == 2
    assert player.points == 1
    assert isinstance(player.cards[1], pokemon.Pokemon)
    player.pick()
    assert len(player.cards) == 3
    assert player.points == 0
    assert isinstance(player.cards[2], pokemon.Pokemon)


def test_ext_api(monkeypatch):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    pokemons = tyradex.get_pokemons()
    assert len(pokemons) == 6


def test_player_pick_fails_connection(monkeypatch):
    monkeypatch.setattr(tyradex, "get_pokemons", _raise_connection_error)

    player = pokemon.Player()
    with pytest.raises(exception.ConnectionError) as exc:
        player.pick()
    assert "Cannot connect to external API" == str(exc.value)


def _raise_connection_error():
    raise exception.ConnectionError("Cannot connect to external API")


def test_player_pick_more_than_3(monkeypatch):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    player = pokemon.Player()
    player.pick()
    player.pick()
    player.pick()
    with pytest.raises(exception.CannotPickMore):
        player.pick()


def test_player_pick_pokemons(monkeypatch, mocker):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    mocker.patch(
        "pokemon.player.random.choice",
        side_effect=[
            fakes.fake_pokemons()[1],
            fakes.fake_pokemons()[4],
            fakes.fake_pokemons()[2],
        ],
    )
    player = pokemon.Player()
    player.pick()
    assert len(player.cards) == 1
    assert player.points == 2
    assert isinstance(player.cards[0], pokemon.Pokemon)
    # id 1
    assert player.cards[0].name == "Bulbizarre"
    player.pick()
    assert len(player.cards) == 2
    assert player.points == 1
    assert isinstance(player.cards[1], pokemon.Pokemon)
    # id 4
    assert player.cards[1].name == "Salamèche"
    player.pick()
    assert len(player.cards) == 3
    assert player.points == 0
    assert isinstance(player.cards[2], pokemon.Pokemon)
    # id 2
    assert player.cards[2].name == "Herbizarre"


def test_show_cards_txt(monkeypatch, mocker):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    mocker.patch(
        "pokemon.player.random.choice", return_value=fakes.fake_pokemons()[1]
    )

    player = pokemon.Player()
    player.pick()
    txt_renderer = card_renderer.TxtCardRenderer()
    viewer = pokemon.PlayerView(player, txt_renderer)
    s = viewer.show_cards()
    print(s)
    assert "Bulbizarre" in s


def test_show_cards_html(monkeypatch, mocker):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    mocker.patch(
        "pokemon.player.random.choice", return_value=fakes.fake_pokemons()[1]
    )

    player = pokemon.Player()
    player.pick()
    html_renderer = card_renderer.HtmlCardRenderer()
    viewer = pokemon.PlayerView(player, html_renderer)
    s = viewer.show_cards()
    print(s)
    assert "<!DOCTYPE html>" in s
    assert "Bulbizarre" in s


def test_show_cards_html_no_evolution(monkeypatch, mocker):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    mocker.patch(
        "pokemon.player.random.choice", return_value=fakes.fake_pokemons()[3]
    )

    player = pokemon.Player()
    player.pick()
    html_renderer = card_renderer.HtmlCardRenderer()
    viewer = pokemon.PlayerView(player, html_renderer)
    s = viewer.show_cards()
    print(s)
    assert "<!DOCTYPE html>" in s
    assert "Florizarre" in s
    assert "Pas d'évolution" in s
