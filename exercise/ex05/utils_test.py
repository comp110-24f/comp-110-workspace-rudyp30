"""ex05 tester"""

__author__ = "730767675"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Unit tests for only_evens"""


def test_only_even_empty() -> None:  # Edge case test
    """If list is empty, return 0"""
    result: list[int] = only_evens([])
    assert len(result) == 0


def test_only_evens_mixed_numbers() -> None:  # Regular Test
    """Checks to make sure no odd numbs left over"""
    list1: list[int] = [1, 2, 3, 3, 3, 6, 7, 9, 10]
    only_evens(list1)  # Should empty out all odds

    result: list[int] = [2, 6, 10]

    assert len(result) != len(list1)


def test_only_evens_all_evens():  # Regular Test
    """Test only_evens with a list of only even numbers."""
    result = only_evens([2, 4, 6, 8])
    expected = [2, 4, 6, 8]
    assert len(result) == len(expected)  # Test length equality
    for idx in range(0, 4):
        assert result[idx] == expected[idx]  # Test each value manually


"""Tests for sub function"""


def test_sub_empty_list():  # Edge Case
    """Test with an empty list"""
    result = sub([], 0, 3)
    assert len(result) == 0  # Ensure result is an empty list


def test_sub_standard_case():  # Normal Test
    """Test sub with a normally"""
    result = sub([10, 20, 30, 40], 1, 3)
    expected = [20, 30]

    for idx in range(len(result)):
        assert result[idx] == expected[idx]  # Test each value


def test_sub_original_list_not_mutated():
    """Sub should not modify its list"""
    original_list: list[int] = [10, 20, 30, 40]
    sub(original_list, 1, 3)  # Uses function on list
    assert len(original_list) == 4  # Make sure length hasnt changed
    assert original_list[0] == 10  # Now check each individual index
    assert original_list[1] == 20
    assert original_list[2] == 30
    assert original_list[3] == 40


"""Tests function add_at_index"""


def test_add_at_index_start_of_list():
    """Test inserts at the start"""
    list1: list[int] = [2, 3, 4]

    add_at_index(list1, 1, 0)
    assert list1[0] == 1  # Ensure the element was added at index 0


def test_add_at_index_length():
    """Make sure it adds a number at least"""
    list1: list[int] = [2, 3, 4]
    add_at_index(list1, 3, 2)
    assert len(list1) == 4


def test_add_at_index_edge_case_empty_list():  # Edge Case
    """Test if the original list was empty"""
    num_list = []
    add_at_index(num_list, 100, 0)  # Valid index for an empty list (0)
    assert num_list[0] == 100  # List should have the added element at index 0


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    list1: list[int] = [2, 3, 4]
    with pytest.raises(IndexError):
        add_at_index(list1, 3, 20)
        # that is greater than the length of our <list_object>
