"""for loop + range"""

# for *variable* in *sequence*:

xs: list[str] = ["w", "x", "y", "z"]

# for elem in xs:
#    print(elem)

pets: list[str] = ["Louie", "Bo", "Bear"]

for pet_names in pets:
    print(f"Good boy, {pet_names}!")

# range(start, end, [step=1]), step=1 is default

# using range is helpful to get the idx of elements
for index in range(0, len(pets)):
    print(f"{index}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
