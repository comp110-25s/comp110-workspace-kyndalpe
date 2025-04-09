"""This assignment will work with making dictionaries."""

__author__ = "730449717"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """This will create a new dictionary that inverts the values and keys."""
    inverteddictionary: dict[str, str] = dict()
    for keys in dictionary:
        if dictionary[keys] in inverteddictionary:
            raise KeyError("error is not permitted")
        inverteddictionary[dictionary[keys]] = keys
    return inverteddictionary


def count(bigstate: list[str]) -> dict[str, int]:
    """This will track each value and the number of times it is included in a list"""
    statecount: dict[str, int] = dict()
    for state in bigstate:
        if state in statecount:
            statecount[state] += 1
        else:
            statecount[state] = 1
    return statecount


def favorite_color(name_color: dict[str, str]) -> str:
    """This will show the most popular color from a collection."""
    favorite: str = ""
    colors: list[str] = []
    for name in name_color:
        colors.append(name_color[name])
    count_colors: dict[str, int] = count(colors)
    max: int = 0
    for keys in count_colors:
        if count_colors[keys] > max:
            max = count_colors[keys]
            favorite = keys
    return favorite


def bin_len(worded_list: list[str]) -> dict[int, set[str]]:
    """This will show the words that are a specific length."""
    words_of_length: dict[int, set[str]] = {}
    for words in worded_list:
        length: int = len(words)
        if length in words_of_length:
            words_of_length[length].add(words)
        else:
            words_of_length[length] = {words}
    return words_of_length
