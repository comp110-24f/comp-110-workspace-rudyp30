"""CQ02"""

__author__ = "730767675"


def guess_a_number() -> None:
    """A function that allows a user to guess a number"""
    secret: int = 7  # set the secret number
    user_guess: str = input("Guess a number:")  # allow user to input
    print("Your guess was " + str(int(user_guess)))
    if int(user_guess) == secret:  # checks for the number first
        print("You got it!")
    elif int(user_guess) < secret:  # back up check if its lower
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(user_guess) > secret:  # back up check if its higher
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
