import copy
import pokemon
import pytest

from pokemon.tests import fakes
from pokemon.ext_api import tyradex
from pokemon import exception


def test_pokemon_instance():
    p = pokemon.Pokemon.from_dict(copy.deepcopy(fakes.fake_pokemons()[1]))
    assert p.name == "Bulbizarre"
    assert p.atk == 49
    assert p.evolution == 2
    assert (
        p.img == "https://raw.githubusercontent.com/Yarkis01/TyraDex/"
        "images/sprites/1/regular.png"
    )
    assert p.type == pokemon.PokemonTypes.PLANTE


def test_pokemon_instance_fails_no_name():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["name"]
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for name_data: 'None' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_instance_fails_no_fr():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["name"]["fr"]
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for name: 'None' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_instance_fails_no_stats():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["stats"]
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for stats: 'None' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_instance_fails_no_atk():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["stats"]["atk"]
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert "The return values for atk: 'None' are not the expected ones" == str(
        exc.value
    )


def test_pokemon_instance_fails_atk_is_not_int():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    fake_pokemon["stats"]["atk"] = "1"
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert "The return values for atk: '1' are not the expected ones" == str(
        exc.value
    )


def test_pokemon_instance_fails_no_evolution():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["evolution"]
    p = pokemon.Pokemon.from_dict(fake_pokemon)
    assert p.name == "Bulbizarre"
    assert p.atk == 49
    assert p.evolution is None
    assert (
        p.img == "https://raw.githubusercontent.com/Yarkis01/TyraDex/"
        "images/sprites/1/regular.png"
    )
    assert p.type == pokemon.PokemonTypes.PLANTE


def test_pokemon_instance_fails_no_evolution_next():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["evolution"]["next"]
    p = pokemon.Pokemon.from_dict(fake_pokemon)
    assert p.name == "Bulbizarre"
    assert p.atk == 49
    assert p.evolution is None
    assert (
        p.img == "https://raw.githubusercontent.com/Yarkis01/TyraDex/"
        "images/sprites/1/regular.png"
    )
    assert p.type == pokemon.PokemonTypes.PLANTE


def test_pokemon_instance_fails_evolution_data_is_not_a_dict():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    fake_pokemon["evolution"] = "1"
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for evolution_data: '1' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_instance_fails_evolution_next_is_not_int():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    fake_pokemon["evolution"]["next"][0]["pokedex_id"] = "5"
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for evolution: '5' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_instance_fails_no_sprites():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["sprites"]
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for img_data: 'None' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_instance_fails_no_sprites_regular():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["sprites"]["regular"]
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert "The return values for img: 'None' are not the expected ones" == str(
        exc.value
    )


def test_pokemon_fails_no_types():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    del fake_pokemon["types"]
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for types_data: 'None' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_fails_types_name_is_not_a_string():
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    fake_pokemon["types"][0]["name"] = 3
    with pytest.raises(ValueError) as exc:
        pokemon.Pokemon.from_dict(fake_pokemon)

    assert (
        "The return values for pokemon_type: '3' are not the expected ones"
        == str(exc.value)
    )


def test_pokemon_evolve(monkeypatch):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    p = pokemon.Pokemon.from_dict(fake_pokemon)
    evolved_p = p.evolve()
    if evolved_p:
        assert evolved_p.name == "Herbizarre"
        assert evolved_p.atk == 62
        assert evolved_p.evolution == 3
        assert (
            evolved_p.img
            == "https://raw.githubusercontent.com/Yarkis01/TyraDex/"
            "images/sprites/2/regular.png"
        )
        assert evolved_p.type == pokemon.PokemonTypes.PLANTE


def test_pokemon_no_evolution(monkeypatch):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[3])
    p = pokemon.Pokemon.from_dict(fake_pokemon)
    evolved_p = p.evolve()
    assert evolved_p is None


def test_pokemon_evolve_fails_pokemon_not_found(monkeypatch):
    monkeypatch.setattr(tyradex, "get_pokemons", fakes.fake_pokemons)
    fake_pokemon = copy.deepcopy(fakes.fake_pokemons()[1])
    fake_pokemon["evolution"]["next"][0]["pokedex_id"] = 10000
    p = pokemon.Pokemon.from_dict(fake_pokemon)
    with pytest.raises(exception.PokemonNotFound) as exc:
        p.evolve()
    assert "Pokemon with id:'10000' not found" == str(exc.value)
