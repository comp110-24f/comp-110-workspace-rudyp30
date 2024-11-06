"""CQ07"""

__author__ = "730767675"


def find_and_remove_max(num_list: list[int]) -> int:
    """Find the largest number in the list"""
    if len(num_list) == 0:  # If empty list
        return -1

    high: int = num_list[0]  # Int set to first number in list
    idx: int = 1  # Set idx at 1 so I can see past 1st num

    while idx < len(num_list):
        if num_list[idx] > high:  # if num is higher than previous
            high = num_list[idx]  # set num to next idx num
        idx += 1

    idx = 0  # Reset index
    while idx < len(num_list):  # Another loop to go through list
        if num_list[idx] == high:  # If the numb is == to high
            num_list.pop(idx)  # Remove the numb at set idx
        else:  # Go onto next if not ==
            idx += 1

    return high


# Test cases
""""
b: list[int] = [10, 9, 8, 7, 10]
print(find_and_remove_max(b))
print(b)

a: list[int] = []
print(find_and_remove_max(a))
print(a)
"""
