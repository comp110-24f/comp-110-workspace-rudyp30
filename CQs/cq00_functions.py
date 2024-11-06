"""CQ00"""

__author__ = "730767675"


def mimic(message: str) -> str:
    """function that will repeat your message"""
    return message


def main() -> None:
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
