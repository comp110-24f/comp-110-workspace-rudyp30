"""Practice w conditionals"""


def less_than_10(num: int) -> None:
    """tell me if num is <10"""
    dub: int = num * 2
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


less_than_10(num=7)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:  # conditional boolean
        print("Eat some food!!")  # then block
    else:
        print("Do ur comp 110 work")  # else block
    print("I'm proud of you")  # either way, prints


# should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> None:
    """Checks whether the given letter matches the first letter of the word"""
    if letter == word[0]:  # checks to see if the letter and first letter of word match
        print("It matches!!")
    else:
        print(
            "Your letter and first letter of word do not match"
        )  # else block if they don't


# check_first_letter(word="Hello", letter="a")
