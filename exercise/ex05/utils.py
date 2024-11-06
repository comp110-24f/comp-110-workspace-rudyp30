"""ex05"""

__author__ = "730767675"


def only_evens(num_list: list[int]) -> list[int]:
    """This function finds evens only in a list"""
    returned_list: list[int] = []  # The list to return
    for numb in num_list:  # Goes through all numbs in list
        if numb % 2 == 0:  # Checks if its even
            returned_list.append(numb)  # If its even, add it to list to return
    return returned_list


# Test case: print(only_evens([1, 2, 3, 4, 5, 6, 8]))


def sub(num_list: list[int], start: int, end: int) -> list[int]:
    """Gives back the list with a inputted index range"""
    if (
        len(num_list) == 0 or start >= len(num_list) or end <= 0
    ):  # If the starts or ends are messed up
        return []

    if start < 0:  # No such thing as -1 idx, so set to 0
        start = 0
    if end > len(num_list):  # Even if end is longer than list, ends at end
        end = len(num_list)  # Creates a gurantee for no "out of index" error

    sub_set_result: list[int] = []  # To make sure original list isnt mutated

    for idx in range(start, end):  # Goes through each elem from given start/end
        sub_set_result.append(num_list[idx])  # Adds it to the returned list

    return sub_set_result


# Test cases for sub
""""
a_list = [10, 20, 30, 40]
b_list = []
print(sub(a_list, -1, 6))
print(sub(b_list, -1, 6))
"""


def add_at_index(num_list: list[int], elem: int, given_idx: int) -> None:
    """Adds specified elem at certain index"""

    if given_idx < 0 or given_idx > len(num_list):  # Error for idx range
        raise IndexError("Index is out of bounds for the input list")

    num_list.append(0)  # For shift purpose

    position: int = (
        len(num_list) - 1
    )  # Set to last idx, helps change the pos and shift numbs

    while given_idx < position:
        num_list[position] = num_list[position - 1]  # Keeps shifting the numbers right
        position -= 1  # Keeps loop going

    num_list[given_idx] = elem  # Once out of loop, mutate duped number to given elem


# Test cases for add_at_idx
""""
list_1 = [1, 2, 3, 5]
print(list_1)
add_at_index(list_1, 4, 3)
print(list_1)
list_3 = []
add_at_index(list_3, 1, 1)
"""
