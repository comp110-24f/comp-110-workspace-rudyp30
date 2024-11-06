"""Summing the elements of a list using different loops"""

__author__ = "730767675"


def w_sum(vals: list[float]) -> float:
    """Adds up all numbs in the list"""
    idx: int = 0
    total: float = 0  # Set for total, will change

    if len(vals) == 0:  # If empty list
        return 0.0

    while idx < len(vals):
        total += vals[idx]
        idx += 1

    return total


def f_sum(vals: list[float]) -> float:
    """Adds up all numbs w for loop"""
    if len(vals) == 0:  # If empty list
        return 0.0

    total: float = 0.0
    for numb in vals:  # Sets numb = vals and adds it to total
        total += numb
    return total


def f_range_sum(vals: list[float]) -> float:
    """Adds up all numbs with a range in the loop"""
    if len(vals) == 0:  # If empty list
        return 0.0

    total: float = 0.0
    for idx in range(0, len(vals)):
        total += vals[idx]
    return total
