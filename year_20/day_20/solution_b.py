
from tests import run_tests
import math

from .classes import Tile


def get_solution(puzzle_input: str):
    tiles = {
        tile.splitlines()[0].split(" ")[1][:-1]: Tile(
            tile.splitlines()[1:], tile.splitlines()[0].split(" ")[1][:-1]
        )
        for tile in puzzle_input.split("\n\n")
    }

    neigbours = Map.get_neighbours(tiles.pop("1951"), tiles)
    print(neigbours)


class Map:
    @classmethod
    def create_map(cls, tiles):
        length = int(math.log(len(tiles), 2))
        grid = [[None for _ in range(length)] for _ in range(length)]
        grid_ids = set()

        for tile in tiles.values():
            print(tile.neighbours(tiles))

    @classmethod
    def get_neighbours(cls, tile: Tile, tiles: dict):
        neighbours = {}

        for border in tile.neighbours(tiles):
            border_id = border[1].tile_id
            if border_id not in tiles:
                continue

            print(border_id, tiles)
            tiles.pop(border_id)
            neighbours[border_id] = cls.get_neighbours(border[1], tiles)

        print("neighbours", neighbours)
        return neighbours


run_tests(func=get_solution, result=2)
