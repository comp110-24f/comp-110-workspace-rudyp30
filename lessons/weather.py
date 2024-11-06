"""If/else statements to check the weather"""


def get_weather_report() -> str:
    """Display weather"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep it cool out there!")
    else:
        print("I don't recognize this weather")
    return weather


get_weather_report()
