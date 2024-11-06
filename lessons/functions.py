"""Practice with functions"""

from random import randint

print(randint(1, 10))


# Function Definition
def sum(num1: int, num2: int) -> int:
    """return the sum of num1 + num2"""
    return num1 + num2


# Function call
print(sum(num1=2, num2=13))
