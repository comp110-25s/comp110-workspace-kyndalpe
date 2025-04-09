"""This game of wordle prompts users to guess a specified word"""

__author__ = "730449717"


def contains_char(word: str, character: str) -> bool:
    """This will determine if a single character is included in the word"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(word):
        if character == word[idx]:
            return True
        else:
            idx = idx + 1
    return False


# The codes below codify the emojis of different colors
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """The emoji provided tells you wheter the guess letter is in the secret word"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    emoji: str = ""
    # This loop checks through every letter in guess and returns a specific color
    while idx < len(guess):
        if secret[idx] == guess[idx]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji


# With a guess, this will tell you wether the guess word is the same length as the expected length
def input_guess(length: int) -> str:
    """This indicated whether the guess word is the same length as the expected length"""
    prompt: str = input(f"Enter a {length} character word:")
    while len(prompt) != length:
        prompt = input(f"That wasn't {length} chars! Try again:")
    return prompt


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    attempts: int = 1
    win: bool = False
    # With each attempt of a new word, if it is not the same length it will allow you to guess another word, but if it is the same length it decreases the amount of attempts that you have remaining
    while attempts < 7 and not win:
        print(f"=== Turn {attempts}/6 ===")
        guess: str = input_guess(len(secret))
        emojis: str = emojified(guess, secret)
        print(emojis)
        if guess == secret:
            win = True
        else:
            attempts = attempts + 1
    if win:
        print(f"You won in {attempts}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
