"""This program will help to plan a tea party and the details of the event.__kyndal__"""

__author__: str = "730449717"


def main_planner(guests: int) -> None:
    """Convert to the number of guests attending the tea party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Convert to number tea bags."""
    return people * 2


def treats(people: int) -> int:
    "Convert to numbers of treats."
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Convert to the cost of tea bags and treats combined."""
    return (tea_count * 1 / 2) + (treat_count * 3 / 4)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
