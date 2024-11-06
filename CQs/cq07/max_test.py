"""CQ07 Test"""

__author__ = "730767675"

from CQs.cq07.find_max import find_and_remove_max


def test_return_value() -> None:
    """Should return my Highest value"""
    numbs: list[int] = [1, 2, 3, 4, 5, 6, 7]

    assert find_and_remove_max(numbs) == 7


def test_mutation() -> None:
    numbs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    old_len_list: int = len(numbs)  # Length of list
    find_and_remove_max(numbs)

    assert old_len_list != len(numbs)  # Compares if it was changed


def test_edge_case() -> None:
    numbs: list[int] = [-10, -20, -5, 0, 5, 10, 10]  # Use negative to make sure

    return_value: int = find_and_remove_max(numbs)  # Should get highest number
    assert return_value == 10

    assert numbs == [-10, -20, -5, 0, 5]  # Makes sure 10s got removed
