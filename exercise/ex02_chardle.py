"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730767675"


def input_word() -> str:
    """Function to allow user to input word"""
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) == 5:  # checks for the length of given word
        print(user_word)
        return user_word
    else:
        print("Error: Word must contain 5 characters.")  # error message for user
        print(user_word)
        quit()  # will quit if not 5 letters


def input_letter() -> str:
    """Function that allows user to input their letter of choice"""
    user_letter: str = input("Enter a single character: ")  # takes in inputted letter
    if len(user_letter) == 1:  # to make sure its only 1 character
        print(user_letter)
        return user_letter
    else:
        print("Error: Character must be a single character.")
        print(user_letter)
        quit()  # quits if its not == 1


def contains_character(input_word: str, input_letter: str) -> None:
    """Function to check through each index for matching characters"""
    matching_characters: int = 0  # initialize variable of # of matches
    print("Searching for " + input_letter + " in " + input_word)
    if input_letter == input_word[0]:  # checks for index 0
        print(input_letter + " found at index 0")
        matching_characters += 1  # used to keep count of amount of matches
    if input_letter == input_word[1]:
        print(input_letter + " found at index 1")
        matching_characters += 1  # using =+1 to make it increasing and clean
    if input_letter == input_word[2]:
        print(input_letter + " found at index 2")
        matching_characters += 1
    if input_letter == input_word[3]:  # checks for index 3
        print(input_letter + " found at index 3")
        matching_characters += 1
    if input_letter == input_word[4]:  # checks for index 4
        print(input_letter + " found at index 4")
        matching_characters += 1
    if matching_characters == 0:  # if there was no matches
        print("No instances of " + input_letter + " found in " + input_word)
    elif matching_characters == 1:
        print(
            str(matching_characters)
            + " instance of "
            + input_letter
            + " found in "
            + input_word
        )
    else:  # if there was a match
        print(
            str(matching_characters)
            + " instances of "
            + input_letter
            + " found in "
            + input_word
        )


def main() -> None:
    word = input_word()
    letter = input_letter()
    contains_character(word, letter)


if __name__ == "__main__":
    main()
