"""Working with dictionaries - ex06"""

__author__ = "730767675"


def invert(diction: dict[str, str]) -> dict[str, str]:
    """Inverts the given dict"""

    inverted_dict: dict[str, str] = {}  # Returned list

    for elem in diction:  # Goes through every key
        new_key: str = diction[elem]  # Grabs the current value to set as new key

        if new_key in inverted_dict:  # Checks if key and is already in new dict
            raise KeyError("There is a Key Error!")

        inverted_dict[new_key] = elem  # Uses new_key and makes value the old key

    return inverted_dict


# Test cases for invert
""""
print(invert({"a": "z", "b": "y", "c": "x"}))
print(invert({"apple": "cat"}))
print(invert({"kris": "jordan", "michael": "jordan"}))
"""


def favorite_color(diction: dict[str, str]) -> str:
    """Returns most common color"""

    if len(diction) == 0:  # Checks for empty dictionaries
        return ""

    most_common: str = ""  # Gonna return
    highest_count: int = 0

    color_count: dict[str, int] = {}  # New dict to see numbers and times mentioned

    for key in diction:
        color_count[diction[key]] = 0  # Adds all the colors to a dict, sets val to 0

    for key in diction:
        color_count[diction[key]] += 1  # Counts times mentioned, changes val

    for color in color_count:
        count = color_count[color]  # Makes current count = to color count
        if count > highest_count:  # If higher than before, changes highest
            most_common = color
            highest_count = count

    return most_common


""""
print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))
"""


def count(input: list[str]) -> dict[str, int]:
    """Gives a dict that shows the count of times the value appeared in input list"""
    result: dict[str, int] = {}  # Returned dict with the count and # of times

    for elem in input:
        if elem in result:
            result[elem] += 1  # After at 1, counts any dupes
        else:
            result[elem] = 1  # Sets all them = to 1 at first

    return result


""""
print(
    count(
        ["Wake", "Wake", "Raleigh", "Asheville", "Canton", "Canton", "Durham", "Wake"]
    )
)
"""


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary with alphabetized keys"""

    result: dict[str, list[str]] = {}  # resulted dict

    for word in input:
        first_letter: str = word[0].lower()  # Get first letter in lowercase
        if first_letter in result:
            result[first_letter].append(word)  # Add to the list, checking with "in"
        else:
            result[first_letter] = [word]  # Initialize the dict's keys

    return result


# print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))


def update_attendance(days: dict[str, list[str]], DoW: str, stud: str) -> None:
    """Adds student attendance to a certain day and keeps a list of the kids"""
    if DoW not in days:  # Check if the day of the week exists in the dictionary
        days[DoW] = []  # If not, create a new list for the day

    if (
        stud not in days[DoW]
    ):  # Check if the student is already in the list for the given day
        days[DoW].append(stud)  # Add the student to the existing list for the day


""""
attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)
"""
