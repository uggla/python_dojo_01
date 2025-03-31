from typing import Self
from dataclasses import dataclass
from enum import Enum


class PokemonTypes(Enum):
    ACIER = "Acier"
    COMBAT = "Combat"
    DRAGON = "Dragon"
    EAU = "Eau"
    ELECTRIK = "Électrik"
    FEE = "Fée"
    FEU = "Feu"
    GLACE = "Glace"
    INSECTE = "Insecte"
    NORMAL = "Normal"
    PLANTE = "Plante"
    POISON = "Poison"
    PSY = "Psy"
    ROCHE = "Roche"
    SOL = "Sol"
    SPECTRE = "Spectre"
    TENEBRES = "Ténèbres"
    VOL = "Vol"


@dataclass
class Pokemon:
    name: str
    atk: int
    evolution: int | None
    img: str
    type: PokemonTypes

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> Self:
        name_data = data.get("name")
        if not isinstance(name_data, dict):
            raise ValueError(
                f"The return values for name_data: '{name_data}' are not the expected ones"
            )

        fr_name = name_data.get("fr")
        if fr_name is None or not isinstance(fr_name, str):
            raise ValueError(
                f"The return values for name: '{fr_name}' are not the expected ones"
            )

        stats = data.get("stats")
        if not isinstance(stats, dict):
            raise ValueError(
                f"The return values for stats: '{stats}' are not the expected ones"
            )

        atk = stats.get("atk")
        if not isinstance(atk, int):
            raise ValueError(
                f"The return values for atk: '{atk}' are not the expected ones"
            )

        evolution_data = data.get("evolution")
        if evolution_data is None:
            evolution = None
        elif isinstance(evolution_data, dict):
            evolutions = evolution_data.get("next")
            if evolutions is None or len(evolutions) == 0:
                evolution = None
            else:
                evolution = evolutions[0].get("pokedex_id")
                if not isinstance(evolution, int):
                    raise ValueError(
                        f"The return values for evolution: '{evolution}' are not the expected ones"
                    )
        else:
            raise ValueError(
                f"The return values for evolution_data: '{evolution_data}' are not the expected ones"
            )

        img_data = data.get("sprites")
        if not isinstance(img_data, dict):
            raise ValueError(
                f"The return values for img_data: '{img_data}' are not the expected ones"
            )

        img = img_data.get("regular")
        if not isinstance(img, str):
            raise ValueError(
                f"The return values for img: '{img}' are not the expected ones"
            )

        types_data = data.get("types")
        if not isinstance(types_data, list) or len(types_data) == 0:
            raise ValueError(
                f"The return values for types_data: '{types_data}' are not the expected ones"
            )

        pokemon_type = types_data[0]["name"]
        if not isinstance(pokemon_type, str):
            raise ValueError(
                f"The return values for pokemon_type: '{pokemon_type}' are not the expected ones"
            )

        pokemon_type = PokemonTypes(pokemon_type)

        return cls(
            name=fr_name,
            atk=atk,
            evolution=evolution,
            img=img,
            type=pokemon_type,
        )
