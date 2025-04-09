#def reverse(item: list[str]) -> list[str]:
    reversed: list[str] = []
    number: int = len(item)
    while number > 0:
        reversed.append(item[number - 1])
        number -= 1
    return reversed


#berev: list[str] = ["ow", "what", "like"]

def flip_flop(about:list[str]) -> None:
    """Swap the current index's value with the next."""
    idx:int=0
    create: list[str]=[]
    while idx < len(about-1):
        create.append(about[idx+1])
        idx+=1
    return None

only: list[str]=["but", "need", "want"]
flip_flop(only)

