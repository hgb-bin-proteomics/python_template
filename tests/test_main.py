#!/usr/bin/env python3

# SCRIPT NAME - TESTS
# 2026 (c) YOUR NAME
# https://github.com/username/
# your.mail@mail.com

import pytest


def test1():
    from streamlit.testing.v1 import AppTest

    at = AppTest.from_file("app.py", default_timeout=30.0)
    at.run(timeout=60.0)
    assert not at.exception


def test2():
    from main import Character

    character = Character(name="John Baldur")
    assert character["name"] == "John Baldur"


def test3():
    from main import Character

    character = Character(name="John Baldur")
    new_character = character.copy_with_update(update={"race": "Human"})
    assert new_character.race == "Human"


def test4():
    from main import Character

    character = Character(name="John Baldur")
    assert character.attack() == pytest.approx(0.0)


def test5():
    from main import character_factory

    characters = character_factory("data/characters.csv")
    assert characters[0].name == "Astarion"


def test6():
    from main import character_factory, battle

    characters = character_factory("data/characters.csv")
    winner = battle(characters[0], characters[1], health=10000)
    assert winner.name == "Shadowheart"


def test7():
    from main import main

    assert main(["-f", "data/characters.csv"]) == 0
