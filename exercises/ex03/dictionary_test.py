"""This file will test the dictionary that was formulated."""

__author__ = "730449717"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use() -> None:
    """Assert that this use case functions properly."""
    inverted: dict[str, str] = {"b": "a", "d": "c", "f": "e"}
    assert invert(inverted) == {"a": "b", "c": "d", "e": "f"}


def test_invert_use1() -> None:
    """Assert that this use case functions properly."""
    inverted: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(inverted) == {"b": "a", "d": "c", "f": "e"}


def test_invert_edge() -> None:
    """Assert that this edge case functions properly."""
    inverted: dict[str, str] = {}
    assert invert(inverted) == {}


def test_count_use() -> None:
    """Assert that this use case functions properly."""
    states: list[str] = ["NC", "SC", "SC", "FL"]
    assert count(states) == {"NC": 1, "SC": 2, "FL": 1}


def test_count_use2() -> None:
    """Assert that this use case functions properly."""
    states: list[str] = ["NC", "GA", "SC", "FL"]
    assert count(states) == {"NC": 1, "GA": 1, "SC": 1, "FL": 1}


def test_count_edge() -> None:
    """Assert that this edge case functions properly."""
    states: list[str] = []
    assert count(states) == {}


def test_favorite_color_use() -> None:
    """Assert that this use case functions properly."""
    people_colors: dict[str, str] = {"Bob": "Blue", "Chi": "Green", "Psy": "Blue"}
    assert favorite_color(people_colors) == ("Blue")


def test_favorite_color_use2() -> None:
    """Assert that this use case functions properly."""
    people_colors: dict[str, str] = {"Sophie": "Grey", "Luke": "Grey", "Izzie": "Black"}
    assert favorite_color(people_colors) == ("Grey")


def test_favorite_color_edge() -> None:
    """Assert that this edge case functions properly."""
    people_colors: dict[str, str] = {}
    assert favorite_color(people_colors) == ""


def test_bin_len_use() -> None:
    """Assert that this use case functions properly."""
    word_list: list[str] = ["the", "quick", "off"]
    assert bin_len(word_list) == {3: {"the", "off"}, 5: {"quick"}}


def test_bin_len_use1() -> None:
    """Assert that this use case functions properly."""
    word_list: list[str] = ["moon", "ran", "tough", "four"]
    assert bin_len(word_list) == {3: {"ran"}, 4: {"moon", "four"}, 5: {"tough"}}


def test_bin_len_edge() -> None:
    """Assert that this edge case functions properly."""
    word_list: list[str] = []
    assert bin_len(word_list) == {}
