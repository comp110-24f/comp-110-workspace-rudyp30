"""Dictionary usage"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

burger: dict[int, str] = dict()
burger[1] = "beef"
burger[2] = "pork"
burger[3] = "chicken"

# len of dict lets us know number of entries
print(len(ice_cream))  # How many ice creams are there?

# Adding mint ice cream
ice_cream["mint"] = 3

# Test if "pbj" is a key in ice_cream
has_pjb: bool = "pbj" in ice_cream  # Will return true or false

# Accessing/Modifying
ice_cream["chocolate"]  # Tells us amount of chocolate orders
ice_cream["mint"] = 4  # Changes value

# Check if key is in a dict
if "chocolate" in ice_cream:
    print(f"There are {ice_cream['chocolate']} orders of chocolate")
else:
    print("There are no orders of chocolate")

# How to remove
ice_cream.pop("strawberry")

# To iterate over every key, use "for in"
# This is way to grab elems of key # the [flavor] is the key not the elem
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")

print(ice_cream)
list1: list[int] = [1, 2, 3]
print(list1)


# How to iterate through each value using a for in loop
def value_exists(diction: dict[str, int], num: int) -> bool:
    for key in diction:
        if diction[key] == num:
            return True
    return False


test_dict: dict[str, int] = {"a": 2, "b": 4, "c": 7, "d": 1}
print(value_exists(test_dict, 2))
