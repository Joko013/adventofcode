from aocd import get_data
from aocd import submit

from env import SESSION


class AOC:
    @classmethod
    def get_data(cls, day: int, year: int) -> str:
        return get_data(day=day, year=year, session=SESSION)

    @classmethod
    def submit(cls, data, part: str, day: int, year: int):
        submit(data, part=part, day=day, year=year, session=SESSION)
