""""Hello"""


def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(msg[idx])
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"

# chars(a)


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):  # checks if the list are the same length
        return False
    # iterates through the list and compares the elements in the index of both lists
    index: int = 0
    while index < len(list_1):  # goes though both lists
        if list_1[index] != list_2[index]:  # if any elements are different return false
            return False
        index += 1

    return True


# print(is_equal([1, 0, 1], [1, 0, 1]))
# print(is_equal([1, 1, 0], [1, 0, 1]))


def odd_and_even(input: list[int]) -> list[int]:
    returned_list: list[int] = []

    for idx in range(0, len(input)):
        if idx % 2 == 0 and input[idx] % 2 == 1:
            returned_list.append(input[idx])

    return returned_list


def count_regs(county: str, reg: list[str]) -> int:
    registered: int = 0
    for person in reg:
        if person == county:
            registered += 1

    return registered
