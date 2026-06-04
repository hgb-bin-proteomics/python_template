#!/usr/bin/env python3
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "polars>=1.41.2",
#   "pydantic>=2.13.4",
# ]
# ///
# PLEASE BE AWARE THAT SCRIPT METADATA WILL OVERRIDE THE PYPROJECT.TOML

from __future__ import annotations

import argparse
import random
import logging
import polars as pl
from pydantic import BaseModel, Field, ConfigDict, computed_field

from typing import Annotated, Optional, Literal, Dict, List, Any, override

__version = "1.0.0"
__date = "2024-03-11"

logger = logging.getLogger(__name__)

r"""
DESCRIPTION:
A description of the script [multiplies two integers].
USAGE:
main.py [-f1 --factor1]
        [-f2 --factor2]
required arguments:
    -f1 int, --factor1 int
        First factor of multiplication.
optional arguments:
    -f2 int, --factor2
        Second factor of multiplication.
        Default: 2
    -h, --help
        Show this help message and exit.
    --version
        Show program's version number and exit.
"""

# these examples use the numpy docstring style
# https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard


class Character(BaseModel):
    name: Annotated[str, Field(frozen=True, description="Name of the character.")]
    r"""
    """
    race: Annotated[
        Optional[Literal["Elf", "Half-Elf", "Human"]],
        Field(frozen=True, description="Race of the character."),
    ] = None
    min_damage: Annotated[
        float, Field(frozen=False, description="Minimum damage the character deals.")
    ] = 0.0
    max_damage: Annotated[
        float, Field(frozen=False, description="Maximum damage the character deals.")
    ] = 0.0

    model_config = ConfigDict(
        validate_assignment=True, strict=True, str_strip_whitespace=True
    )
    r"""
    Pydantic configuration for the underlying validation model.
    """

    @computed_field(description="Average damage dealt by the character.")
    @property
    def avg_damage(self) -> float:
        r"""
        Average damage dealt by the character.
        """
        return (self.min_damage + self.max_damage) / 2.0

    @override
    def model_post_init(self, context: Any = None) -> None:
        r"""
        Performs extra validation and post init functions.

        Warnings
        --------
        This method should not be called manually!
        """
        if self.min_damage > self.max_damage:
            self.__dict__["min_damage"], self.__dict__["max_damage"] = (
                self.max_damage,
                self.min_damage,
            )

    def __getitem__(self, key: str) -> Any:
        r"""
        Support for dict-like access.
        """
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(f"'{key}' is not a valid field!")

    def __contains__(self, key: str) -> bool:
        r"""
        Support for ``in`` operator.
        """
        return hasattr(self, key)

    def copy_with_update(self, update: Dict[str, Any] = {}) -> Character:
        return Character(
            name=update["name"] if "name" in update else self.name,
            race=update["race"] if "race" in update else self.race,
            min_damage=update["min_damage"]
            if "min_damage" in update
            else self.min_damage,
            max_damage=update["max_damage"]
            if "max_damage" in update
            else self.max_damage,
        )

    def attack(self) -> float:
        return self.min_damage + (self.max_damage - self.min_damage) * random.random()


def character_factory(filename: str) -> List[Character]:
    df = pl.read_csv(filename)
    characters: List[Character] = list()
    for row in df.iter_rows(named=True):
        characters.append(
            Character(
                name=str(row["name"]),
                race=str(row["race"]) if "race" in row else None,  # ty: ignore[invalid-argument-type]
                min_damage=float(row["min_damage"]),
                max_damage=float(row["max_damage"]),
            )
        )
    return characters


def battle(
    character1: Character, character2: Character, health: float = 100.0
) -> Character:
    health1 = health
    health2 = health
    initiative = random.random()
    if initiative < 0.5:
        logger.info(f"Character {character1.name} has initiative!")
    else:
        logger.info(f"Character {character2.name} has initiative!")
    while True:
        if initiative < 0.5:
            attack: float = character1.attack()
            logger.info(f"Character {character1.name} deals {attack} damage!")
            health2 = health2 - attack
            if health2 <= 0:
                break
            attack: float = character2.attack()
            logger.info(f"Character {character2.name} deals {attack} damage!")
            health1 = health1 - attack
            if health1 <= 0:
                break
        else:
            attack: float = character2.attack()
            logger.info(f"Character {character2.name} deals {attack} damage!")
            health1 = health1 - attack
            if health1 <= 0:
                break
            attack: float = character1.attack()
            logger.info(f"Character {character1.name} deals {attack} damage!")
            health2 = health2 - attack
            if health2 <= 0:
                break
    if health1 <= 0:
        logger.info(f"Character {character2.name} won!")
        return character2
    logger.info(f"Character {character1.name} won!")
    return character1


##### MAIN FUNCTION #####


def main(argv: Optional[List[str]] = None) -> int:
    """Main function.

    Parameters
    ----------
    argv : list, default = None
        Arguments passed to argparse.

    Returns
    -------
    product : int
        The product of given arguments.

    Examples
    --------
    >>> from main import main
    >>> product = main(["-f1", "1", "-f2", "2"])
    >>> product
    2
    >>> product = main(["-f1", "3"])
    >>> product
    6
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        required=True,
        help="Character file to read characters from.",
        type=str,
    )
    parser.add_argument(
        "-c1",
        "--character1",
        dest="c1",
        default=0,
        help="First character to use.",
        type=int,
    )
    parser.add_argument(
        "-c2",
        "--character2",
        dest="c2",
        default=1,
        help="Second character to use.",
        type=int,
    )
    parser.add_argument(
        "-hp",
        "--hit-points",
        dest="health",
        default=130,
        help="Second character to use.",
        type=int,
    )
    parser.add_argument("--version", action="version", version=__version)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO)

    try:
        characters = character_factory(args.file)
        c1 = int(args.c1)
        c2 = int(args.c2)
        health = float(args.health)
        logger.info(f"Both characters have {health} hit points! The battle begins:")
        if c1 < 0 or c1 >= len(characters):
            raise IndexError("Character 1 is not a valid index in the character file!")
        if c2 < 0 or c2 >= len(characters):
            raise IndexError("Character 1 is not a valid index in the character file!")
        _ = battle(characters[c1], characters[c2], health)
    except Exception as _e:
        logger.exception("An error occurred while running the script!")
        return 1

    return 0


######## SCRIPT #########


if __name__ == "__main__":
    m = main()
