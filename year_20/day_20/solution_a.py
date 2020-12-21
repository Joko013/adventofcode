from tests import run_tests

from .classes import Tile


def get_solution(puzzle_input: str):
    tiles = {
        tile.splitlines()[0].split(" ")[1][:-1]: Tile(
            tile.splitlines()[1:], tile.splitlines()[0].split(" ")[1][:-1]
        )
        for tile in puzzle_input.split("\n\n")
    }

    result = 1
    for tile_id, tile in tiles.items():
        borders = [
            tile.borders(other) for other_id, other in tiles.items() if tile_id != other_id and tile.borders(other)
        ]
        if len([border for border in borders if border]) == 2:
            result *= int(tile_id)

    return result


run_tests(func=get_solution, result=20899048083289)
