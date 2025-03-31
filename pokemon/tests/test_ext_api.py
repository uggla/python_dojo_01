import pytest
import requests

from pokemon import exception
from pokemon.ext_api import tyradex
from pokemon.tests import fakes


def _fake_requests(_):
    return fakes.fake_requests()


def _raise_connection_error(_):
    raise requests.exceptions.RequestException


def test_ext_api(monkeypatch):
    # Warning we need to clear the cache to ensure the monkeypatch is used
    tyradex.get_pokemons.cache_clear()
    monkeypatch.setattr("pokemon.ext_api.tyradex.requests.get", _fake_requests)
    pokemons = tyradex.get_pokemons()
    assert len(pokemons) == 6


def test_ext_api_fails_connection(monkeypatch):
    # Warning we need to clear the cache to ensure the monkeypatch is used
    tyradex.get_pokemons.cache_clear()
    monkeypatch.setattr(
        "pokemon.ext_api.tyradex.requests.get", _raise_connection_error
    )
    with pytest.raises(exception.ConnectionError) as exc:
        tyradex.get_pokemons()
    assert "Cannot connect to external API" == str(exc.value)
