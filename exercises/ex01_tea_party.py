"""ex01"""

__author__ = "730767675"


def main_planner(guests: int) -> None:
    """planning function to smoothly run the code"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))  # had to convert int -> str
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests)))
    )  # set guests = people


def tea_bags(people: int) -> int:
    """Counts number of tea bags needed"""
    return people * 2  # each person gets 2 tea bags


def treats(people: int) -> int:
    """Returns number of treats per person"""
    return int(
        tea_bags(people=people) * 1.5
    )  # have to do 1.5x tea bags incase people drink more


def cost(tea_count: int, treat_count: int) -> float:
    """adds up the total cost of tea bags + treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
