"""Mutating Functions"""

__author__ = "730767675"


def manual_append(int_list: list, int) -> None:
    int_list.append(int)


def double(int_list: list[int]) -> None:
    idx: int = 0
    while idx < len(int_list):
        int_list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
