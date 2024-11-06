"""EX03 - Wordle - Make 6 guesses at the secret word"""

__author__ = "730767675"


def input_guess(secret_word_len: int) -> str:
    """Makes sure the user's guess is 5 characters"""
    while True:  # infinite loop unless broken
        user_guess: str = input(f"Enter a {secret_word_len} character word: ")
        if len(user_guess) == secret_word_len:
            return user_guess  # allows us to exit the while True loop
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: {user_guess}")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """searches through a given string for a given letter"""
    assert len(char_guess) == 1  # makes sure char_guess is == 1 len

    idx: int = 0
    while idx < len(secret_word):  # loop to look through all of secret_word
        if char_guess == secret_word[idx]:  # checks each index of word
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """will notify on the matches between the guessed word and secret word"""
    assert len(guess) == len(secret)

    # assigning sqaures to variables for easy use
    green_sqr: str = "\U0001F7E9"
    white_sqr: str = "\U00002B1C"
    yellow_sqr: str = "\U0001F7E8"

    coded_result: str = ""  # variable that will produce output
    idx: int = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            coded_result += green_sqr  # adds green sqaure if correct
        elif contains_char(
            secret, guess[idx]
        ):  # use contains_char to compare char w/ str
            coded_result += yellow_sqr
        else:
            coded_result += white_sqr
        idx += 1  # add idx so loop stops
    return coded_result


def main(secret: str) -> None:
    """The games entry point and game loop"""
    turn: int = 1

    while turn <= 6:  # the games whole system basically
        print(f"=== Turn {turn}/6 ===")  # prints the turn
        word_guessed: str = input_guess(len(secret))

        coded_result: str = emojified(word_guessed, secret)
        print(coded_result)

        if word_guessed == secret:  # if you won
            print(f"You won in {turn}/6 turns!")
            return

        turn += 1  # counts the number of turns

    print("X/6 - Sorry, try again tomorow!")


if __name__ == "__main__":
    main(secret="codes")
