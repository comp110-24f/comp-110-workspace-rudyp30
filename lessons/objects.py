"""Object-Oriented Programming (OOP)"""

# Every object has a type and internal data rep
# Object is an instance of a type. IE. 23 is an instance of int


class Profile:  # Capatalize name
    username: str  # Declaring attributes
    bio: str
    followers: int
    follwoing: int
    private: bool

    def __init__(self):  # Initialize attributes. What are default values?
        self.username = ""
        self.bio = ""
        self.followers = 0
        self.following = 0
        self.private = False


my_prof: Profile = Profile()  # Make a new profile!
your_prof: Profile = Profile()
your_prof.username = "COMP110"
my_prof.username = "Alyssa"

print(my_prof.username)


class Burgers:
    meat: str
    cheese: bool
    topping: int
    fries: bool

    def __init__(self):
        self.meat = "beef"
        self.cheese = False
        self.topping = 0
        self.fries = False

    def get_price(self):
        """Get the price of the burger"""
        price: float = 5.0
        if self.cheese:
            price += 1.0
        price += 0.25 * self.topping
        if self.fries is True:
            price += 2
        return price


ur_burger: Burgers = Burgers()
ur_burger.cheese = True
ur_burger.topping = topping = 2

my_burger: Burgers = Burgers()
my_burger.fries = True

print(f"${ur_burger.get_price()}")
print(f"${my_burger.get_price()}")
