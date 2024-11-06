"""Practice with lists"""

# listname: list[item_type]

# empty lists
grocery_list: list[str] = list()
my_numbers: list[float] = []

# To add to a list -> listname.append(item)
my_numbers.append(1.5)
my_numbers.append(2.7)

# print(my_numbers)

# Creating a already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)  # Print whole
print(game_points[2])  # Print specific

# modifying a list
game_points[1] = 72  # changes 86 -> 72
print(game_points)

# Amount of items in a list
print(len(game_points))

# How to remove
game_points.pop(1)
print(game_points)


def display(int_list: list[int]) -> None:
    idx: int = 0
    while idx < len(int_list):
        print(int_list[idx])
        idx += 1


display(game_points)
