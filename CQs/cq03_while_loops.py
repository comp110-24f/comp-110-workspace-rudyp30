"""CQ03"""

__author__ = "730767675"


def num_instances(phrase: str, search_char: str) -> int:
    """A function to check for matching letters in a phrase"""
    count: int = 0  # checks for amount of matches
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
        index += 1  # increases so that we can stop the loop after reading
    return count  # returns our # of matches
