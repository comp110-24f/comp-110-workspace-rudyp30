__author__ = "730767675"


def concat(msg1: str, msg2: str) -> str:
    """Combines 2 strings"""
    combined: str = msg1 + msg2  # new variable to hold combined
    return combined


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
