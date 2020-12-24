from tests import run_tests
import re


def get_solution(puzzle_input: str):
    offsets = {
        "e": complex(1, 0),
        "w": complex(-1, 0),
        "se": complex(0.5, -0.5),
        "sw": complex(-0.5, -0.5),
        "ne": complex(0.5, 0.5),
        "nw": complex(-0.5, 0.5)
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

    for _ in range(100):
        new_tiles = {}

        for position, value in tiles.items():
            b_neighbours = sum(tiles.get(position + offset, False) for offset in offsets.values())

            if value and (b_neighbours == 0 or b_neighbours > 2):
                new_value = False
            elif not value and b_neighbours == 2:
                new_value = True
            else:
                new_value = value

            new_tiles[position] = new_value

            for neighbour_offset in offsets.values():
                b_neighbours = sum(
                    tiles.get(position + neighbour_offset + offset, False) for offset in offsets.values()
                )

                neighbour_value = tiles.get(position + neighbour_offset, False)
                if neighbour_value and (b_neighbours == 0 or b_neighbours > 2):
                    new_value = False
                elif not neighbour_value and b_neighbours == 2:
                    new_value = True
                else:
                    new_value = neighbour_value

                new_tiles[position + neighbour_offset] = new_value

        tiles = new_tiles

    return sum(tiles.values())


run_tests(func=get_solution, result=2208)
