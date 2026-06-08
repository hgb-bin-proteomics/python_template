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

# SCRIPT NAME
# 2026 (c) YOUR NAME
# https://github.com/username/
# your.mail@mail.com

r"""Battles two characters.

.. code-block:: text
   :caption: Example Usage

   usage: main.py [-h] -f FILE [-c1 CHARACTER_1] [-c2 CHARACTER_2] [-hp HEALTH] [--version]

   Battles two characters.

   options:
     -h, --help            show this help message and exit
     -f, --file FILE       character file to read characters from (str).
     -c1, --character-1 CHARACTER_1
                           index of the first character to use (int).
     -c2, --character-2 CHARACTER_2
                           index of the second character to use (int).
     -hp, --hit-points HEALTH
                           health of all characters (int).
     --version             show program's version number and exit

   (c) Micha Birklbauer, 2026
"""

from __future__ import annotations

import argparse
import random
import logging
import polars as pl
from pydantic import BaseModel, Field, ConfigDict, computed_field

from typing import Annotated, Optional, Literal, Any, override

__version = "2.0.0"
__date = "2026-06-05"

logger = logging.getLogger(__name__)

# these examples use the numpy docstring style
# https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard


class Character(BaseModel):
    r"""Core data structure representing a character.

    Bases Pydantic `BaseModel <https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel>`_.

    Attributes Summary
    ------------------
    Here is a short summary about the class attributes, for more details
    on the specific Pydantic validation requirements please refer to the corresponding attributes
    themselves.

    Required
    ^^^^^^^^
    The following attributes are required:

    name : str
        The name of the character.

    Optional
    ^^^^^^^^
    The following attributes are optional:

    race : one of "Elf", "Half-Elf", "Human", or None, default = None
        The race of the character. Should be one of Elf, Half-Elf, or Human.
    min_damage : float, default = 0.0
        Minimum damage the character deals.
    max_damage : float, default = 0.0
        Maximum damage the character deals.

    Notes
    -----
    Minimum and maximum damage are automatically switched depending on which is
    greater.

    Examples
    --------
    >>> from main import Character
    >>> character = Character(name="John Baldur")
    """

    name: Annotated[str, Field(frozen=True, description="Name of the character.")]
    r"""
    Name of the character.
    """
    race: Annotated[
        Optional[Literal["Elf", "Half-Elf", "Human"]],
        Field(frozen=True, description="Race of the character."),
    ] = None
    r"""
    Race of the character. Should be one of Elf, Half-Elf, or Human.
    """
    min_damage: Annotated[
        float, Field(frozen=False, description="Minimum damage the character deals.")
    ] = 0.0
    r"""
    Minimum damage the character deals. Is automatically switched with max_damage
    if max_damage is smaller.
    """
    max_damage: Annotated[
        float, Field(frozen=False, description="Maximum damage the character deals.")
    ] = 0.0
    r"""
    Maximum damage the character deals. Is automatically switched with min_damage
    if min_damage is greater.
    """

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
            self.__dict__["min_damage"], self.__dict__["max_damage"] = (  # pyright: ignore[reportIndexIssue]
                self.max_damage,
                self.min_damage,
            )

    def __getitem__(self, key: str) -> Any:
        r"""
        Support for dict-like access.
        """
        try:
            return getattr(self, key)
        except AttributeError as e:
            raise KeyError(f"'{key}' is not a valid field!") from e

    def __contains__(self, key: str) -> bool:
        r"""
        Support for ``in`` operator.
        """
        return hasattr(self, key)

    def copy_with_update(self, update: dict[str, Any] = {}) -> Character:
        r"""Creates a deep copy of the class with optional attribute updates.

        Parameters
        ----------
        update : dict of str, any, default = empty dict
            Dictionary mapping attribute names (str) to their updated values.
            The default (empty dict) will create a deep copy with the original
            attribute values.

        Returns
        -------
        Character
            New character with optionally updated attributes.

        Examples
        --------
        >>> from main import Character
        >>> character = Character(name="John Baldur")
        >>> new_character = character.copy_with_update(update={"race": "Human"})
        """
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
        r"""Get the attack damage of the next attack.

        Returns
        -------
        float
            The attack damage of the attack.

        Examples
        --------
        >>> from main import Character
        >>> character = Character(name="John Baldur")
        >>> character.attack()
        0.0
        """
        return self.min_damage + (self.max_damage - self.min_damage) * random.random()  # noqa: S311


def character_factory(filename: str) -> list[Character]:
    r"""Creates a list of characters from a file.

    Parameters
    ----------
    filename : str
        The filename of the character ``csv`` file.

    Returns
    -------
    lisf of Character
        The parsed list of characters.

    Examples
    --------
    >>> from main import character_factory
    >>> characters = character_factory("data/characters.csv")
    >>> characters[0].name
    'Astarion'
    """
    df = pl.read_csv(filename)
    characters: list[Character] = list()
    for row in df.iter_rows(named=True):
        characters.append(
            Character(
                name=str(row["name"]),
                race=str(row["race"]) if "race" in row else None,  # pyright: ignore[reportArgumentType] # ty: ignore[invalid-argument-type]
                min_damage=float(row["min_damage"]),
                max_damage=float(row["max_damage"]),
            )
        )
    return characters


def battle(
    character_1: Character, character_2: Character, health: float = 100.0
) -> Character:
    r"""Makes two characters fight.

    Parameters
    ----------
    character_1 : Character
        One of the two characters that should battle.
    character_2 : Character
        One of the two characters that should battle.
    health : float, default = 100.0
        The amount of hit points both characters have.

    Returns
    -------
    Character
        The winner of the two characters.

    Examples
    --------
    >>> from main import character_factory, battle
    >>> characters = character_factory("data/characters.csv")
    >>> winner = battle(characters[0], characters[1], health=10000)
    >>> winner.name
    'Shadowheart'
    """
    health_1 = health
    health_2 = health
    initiative = random.random()  # noqa: S311
    if initiative < 0.5:
        logger.info(f"Character {character_1.name} has initiative!")
    else:
        logger.info(f"Character {character_2.name} has initiative!")
    while True:
        if initiative < 0.5:
            attack: float = character_1.attack()
            logger.info(f"Character {character_1.name} deals {attack} damage!")
            health_2 -= attack
            if health_2 <= 0:
                break
            attack: float = character_2.attack()
            logger.info(f"Character {character_2.name} deals {attack} damage!")
            health_1 -= attack
            if health_1 <= 0:
                break
        else:
            attack: float = character_2.attack()
            logger.info(f"Character {character_2.name} deals {attack} damage!")
            health_1 -= attack
            if health_1 <= 0:
                break
            attack: float = character_1.attack()
            logger.info(f"Character {character_1.name} deals {attack} damage!")
            health_2 -= attack
            if health_2 <= 0:
                break
    if health_1 <= 0:
        logger.info(f"Character {character_2.name} won!")
        return character_2
    logger.info(f"Character {character_1.name} won!")
    return character_1


##### MAIN FUNCTION #####


def main(argv: Optional[list[str]] = None) -> int:
    """Main function.

    Parameters
    ----------
    argv : list or str, or None, default = None
        Arguments passed to argparse.

    Returns
    -------
    int
        Exit status (zero is success).

    Examples
    --------
    >>> from main import main
    >>> main(["-f", "data/characters.csv"])
    INFO:main:Both characters have 130.0 hit points! The battle begins:
    INFO:main:Character Shadowheart has initiative!
    INFO:main:Character Shadowheart deals 311.13673321167755 damage!
    INFO:main:Character Shadowheart won!
    0
    """

    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Battles two characters.",
        epilog="(c) Micha Birklbauer, 2026",
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        required=True,
        help="character file to read characters from (str).",
        type=str,
    )
    parser.add_argument(
        "-c1",
        "--character-1",
        dest="character_1",
        default=0,
        help="index of the first character to use (int).",
        type=int,
    )
    parser.add_argument(
        "-c2",
        "--character-2",
        dest="character_2",
        default=1,
        help="index of the second character to use (int).",
        type=int,
    )
    parser.add_argument(
        "-hp",
        "--hit-points",
        dest="health",
        default=130,
        help="health of all characters (int).",
        type=int,
    )
    parser.add_argument("--version", action="version", version=__version)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO)

    try:
        characters = character_factory(args.file)
        character_1 = int(args.character_1)
        character_2 = int(args.character_2)
        health = float(args.health)
        logger.info(f"Both characters have {health} hit points! The battle begins:")
        if character_1 < 0 or character_1 >= len(characters):
            raise IndexError("Character 1 is not a valid index in the character file!")
        if character_2 < 0 or character_2 >= len(characters):
            raise IndexError("Character 1 is not a valid index in the character file!")
        _ = battle(characters[character_1], characters[character_2], health)
    except Exception as _e:
        logger.exception("An error occurred while running the script!")
        return 1

    return 0


######## SCRIPT #########


if __name__ == "__main__":
    m = main()
