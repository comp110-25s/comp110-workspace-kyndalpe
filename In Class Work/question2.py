def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False
    if word[idx] != secret[idx]:
        print(f"{word[idx]} isn't the secret's word next letter.")
        return False
    else:
        return guess_secret(word=word, secret=secret, idx=idx + 1)
    print("They are the same word!")
    return True


def fizzbuzz(n: int) -> str:
    if n % 3 == 0:
        if n % 5 == 0:
            return "fizzbuzz"
        else:
            return "fizz"
    if n % 5 == 0:
        return "buzz"
    else:
        return str(n)


fizzbuzz(10)
