"""EX04 - List Util - Working backwards!"""

__author__ = "730767675"


def all(num_list: list[int], match: int) -> bool:
    """Checks whether a # matches a whole list of #s"""
    if len(num_list) == 0:
        return False

    idx: int = 0  # Set the index
    all_match: int = 0  # This number will determine if all match or no

    while idx < len(num_list):  # Set loop
        if num_list[idx] == match:
            all_match += 1  # If they match, add to all_match detector
        idx += 1

    if all_match == len(num_list):  # If they all matched, should be == len of list
        return True
    else:
        return False


# Test cases for all
""""
print(all([1, 2, 3], 1))
print(all([1, 1, 1], 2))
print(all([1, 1, 1], 1))
"""


def max(num_list: list[int]) -> int:
    """Find the largest number in the list"""
    high: int = num_list[0]  # Int set to first number in list
    idx: int = 1  # Set idx at 1 so I can see past 1st num

    if len(num_list) == 0:  # Error case
        raise ValueError("max() arg is an empty List")

    while idx < len(num_list):
        if num_list[idx] > high:  # if num is higher than previous
            high = num_list[idx]  # set num to next idx num
        idx += 1
    return high


# Test cases for max
""""
print(max([]))
print(max([1, 3, 2]))
print(max([100, 99, 98]))
print(max([-5, -2, -3, -1]))
"""


def is_equal(input1: list[int], input2: list[int]) -> bool:
    "Checks whether 2 lists match or not"
    if len(input1) != len(input2):  # Check if the lists have diff len
        return False

    idx: int = 0
    while idx < len(input1):  # Go through both lists
        if input1[idx] != input2[idx]:  # If =!, return False
            return False
        idx += 1
    return True  # If == at all, returns True


# Test cases for is_equal
"""""

print(is_equal([1, 0, 1], [1, 0, 1]))
print(is_equal([1, 1, 0], [1, 0, 1]))
"""


def extend(input1: list[int], input2: list[int]) -> None:
    """Takes input2 and adds it to input1"""
    idx: int = 0
    while idx < len(input2):
        input1.append(input2[idx])  # Adds idx of i2 to i1
        idx += 1


# Test cases for extend
"""""
a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
extend(a, b)
print(a)
c: list[int] = [7, 8]
extend(c, b)
print(c)
"""
