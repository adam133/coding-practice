from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from enum import Enum


class UserInput(BaseModel):
    year: int = Field(..., gt=1925, lt=datetime.now().year)


class Generations:
    def __init__(self):
        self.list: list[tuple[str, int, int]] = [
            ("Traditionalists", 1925, 1946),
            ("Baby Boomers", 1947, 1964),
            ("Generation X", 1965, 1981),
            ("Millenials", 1982, 1995),
            ("Generation Z", 1996, 2015),
        ]

    def get_generation(self, year: int) -> str:
        for generation in self.list:
            if generation[1] <= year <= generation[2]:
                return generation[0]
        return "Unknown"


def main():
    print("Hello from day9!")

    user_input_str = input("Enter your year of birth: ")
    try:
        user_input = UserInput(year=user_input_str)
    except ValidationError as e:
        if "Input should be less than 2025" in str(e):
            print("Sorry, you are too young to be born yet!")
        elif "Input should be greater than 1925" in str(e):
            print("Sorry, you are too old!")
        else:
            print(e)
        return

    generations = Generations()

    print(generations.get_generation(user_input.year))


if __name__ == "__main__":
    main()
