"""File to define Fish class."""

__author__ = "730767675"


class Fish:
    """The class for all things fishy."""

    age: int  # Attribute set up

    def __init__(self):
        """Creates a fish with ease."""
        self.age = 0
        return None

    def one_day(self):
        """Simulates DiL of a fishy!"""
        self.age += 1
        return None
