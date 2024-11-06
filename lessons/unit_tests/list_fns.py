"""List functions for unit testing"""


def get_first(input: list[str]) -> str:

    return input[0]


def remove_first(input: list[str]) -> None:
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    first: str = input[0]
    input.pop(0)
    return first


hi: list[str] = ["hi", "hello", "no"]
print(get_and_remove_first(hi))
print(hi)
