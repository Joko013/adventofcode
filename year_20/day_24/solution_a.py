from tests import run_tests
import re


def get_solution(puzzle_input: str):
    offsets = {
        "e": complex(1, 0),
        "w": complex(-1, 0),
        "se": complex(0.5, -0.5),
        "sw": complex(-0.5, -0.5),
        "ne": complex(0.5, 0.5),
        "nw": complex(-0.5, 0.5),
    }
    instructions = puzzle_input.splitlines()
    tiles = {}

    for line in instructions:
        position = complex(0, 0)

        while line:
            match = re.match(r"se|sw|ne|nw|e|w", line)
            position += offsets[match[0]]
            line = line[len(match[0]):]

        tiles[position] = not tiles.get(position, False)

    return sum(tiles.values())


run_tests(func=get_solution, result=10)
