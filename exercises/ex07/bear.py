"""File to define Bear class."""

__author__ = "730767675"


class Bear:
    """Class that creates bears!"""

    age: int  # Age creation
    hunger_score: int

    def __init__(self):
        """Sets up the bears attributes automatically!"""
        self.age = 0  # Set age to 0
        self.hunger_score = 0  # Hunger also at 0
        return None

    def one_day(self):
        """Simulates the day in the life of a bear."""
        self.age += 1  # After 1 day, age goes up and hunger score up
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Allows the bear to up its hunger score."""
        self.hunger_score += num_fish  # 1 fish = +1 score
        return None
