"""File to define River class."""

__author__ = "730767675"
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Runs the river as a whole, combining fish and bear."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish/bears too old."""
        surv_fish: list[Fish] = []  # The surviving animals
        surv_bears: list[Bear] = []

        for bear in self.bears:  # Goes through bears age
            if bear.age <= 5:
                surv_bears.append(bear)

        for fish in self.fish:  # Checks through the fish ages
            if fish.age <= 3:
                surv_fish.append(fish)

        self.fish = surv_fish
        self.bears = surv_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes any number of fish specified."""
        idx: int = 0
        # Make sure add a check for if any fish r avaliable
        while idx < amount and len(self.fish) > 0:  # Removes the fish using a loop.
            self.fish.pop(0)
            idx += 1

    def bears_eating(self):
        """Allows each bear to eat 3 fish if there are >= 5 fish."""
        for (
            bear
        ) in self.bears:  # Check if there are at least 5 fish for the bear to eat
            if len(self.fish) >= 5:
                self.remove_fish(3)  # Remove 3 fish from the river
                bear.eat(3)  # Call the bear's eat method for 3 fish
            else:
                break  # Stops the if statements

        return None

    def check_hunger(self):
        """Checks for starved bears :(."""
        not_starved: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                not_starved.append(bear)

        self.bears = not_starved

        return None

    def repopulate_fish(self):
        """Adds back to fish population."""
        new_fish: int = (len(self.fish) // 2) * 4

        amt_added: int = 0  # Basically a IDX to track loop

        while amt_added < new_fish:  # Loop adds the off spring of fish
            self.fish.append(Fish())
            amt_added += 1
        return None

    def repopulate_bears(self):
        """Adds back to the bear population."""
        new_bears: int = len(self.bears) // 2

        amt_added: int = 0  # Basically a IDX to track loop

        while amt_added < new_bears:  # Loop adds the off spring of bears
            self.bears.append(Bear())
            amt_added += 1
        return None

    def view_river(self):
        """Describes the river environment."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Does 7 days of sim."""
        idx: int = 0

        while idx < 7:  # = so that it does 7 days
            self.one_river_day()
            idx += 1

        return None
