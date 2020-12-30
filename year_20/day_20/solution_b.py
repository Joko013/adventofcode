
from tests import run_tests
import math
import re

from .classes import Tile


def get_solution(puzzle_input: str):
    tiles = {
        tile.splitlines()[0].split(" ")[1][:-1]: Tile(
            tile.splitlines()[1:], tile.splitlines()[0].split(" ")[1][:-1]
        )
        for tile in puzzle_input.split("\n\n")
    }

    map_ = Map(tiles)

    for grid in map_.grid_rotations():
        monsters = map_.find_monsters(grid)

        if monsters > 1:
            break

    # one monster is 15*#
    rough_waters = sum(row.count("#") for row in map_.inner_grid) - (15 * monsters)
    return rough_waters


class Map:
    def __init__(self, tiles):
        self.grid = self.create_grid(tiles)

    @classmethod
    def create_grid(cls, tiles):
        size = int(math.sqrt(len(tiles)))
        grid = [[None for _ in range(size)] for _ in range(size)]

        top_left = cls.get_top_left_tile(tiles)
        grid[0][0] = top_left
        tiles.pop(top_left.tile_id)

        for i in range(size):
            for j in range(size):
                tile = grid[i][j]
                neighbours = tile.neighbours(tiles)

                if i + 1 < size and grid[i + 1][j] is None:
                    vertical = neighbours.get("up")
                    if vertical:
                        grid[i + 1][j] = vertical.rotate_clockwise().rotate_clockwise().flip()
                    else:
                        vertical = neighbours.get("down")
                        grid[i + 1][j] = vertical
                    tiles.pop(vertical.tile_id)

                if j + 1 < size and grid[i][j + 1] is None:
                    horizontal = neighbours.get("left")
                    if horizontal:
                        grid[i][j + 1] = horizontal.flip()
                    else:
                        horizontal = neighbours.get("right")
                        grid[i][j + 1] = horizontal

                    tiles.pop(horizontal.tile_id)

        return grid

    @classmethod
    def get_top_left_tile(cls, tiles):
        for tile in tiles.values():
            neighbours = tile.neighbours(other_tiles=tiles)

            if len(neighbours) == 2 and all(direction in neighbours for direction in ["right", "down"]):
                return tile

            elif len(neighbours) == 2 and all(direction in neighbours for direction in ["left", "up"]):
                return tile.rotate_clockwise().rotate_clockwise()

    @property
    def inner_grid(self):
        inner = list()
        for row in self.grid:
            inner_rows = [tile.inner.rows for tile in row]
            inner.extend(["".join(tup) for tup in list(zip(*inner_rows))])
        return inner

    @staticmethod
    def find_monsters(inner_grid):
        monsters = 0

        for i in range(len(inner_grid) - 2):
            tops = re.finditer(r"(?=([.#]{18}#[.#]))", inner_grid[i])

            for top in tops:
                mid_string = inner_grid[i + 1][top.span(1)[0]:top.span(1)[1]]
                mid = re.match(r"#[.#]{4}##[.#]{4}##[.#]{4}###", mid_string)

                bot_string = inner_grid[i + 2][top.span(1)[0]:top.span(1)[1]]
                bot = re.match(r"[.#]#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{3}", bot_string)

                if mid and bot:
                    monsters += 1

        return monsters

    @staticmethod
    def flip_grid(grid):
        return [line[::-1] for line in grid]

    @staticmethod
    def rotate_grid(grid):
        rows = []
        for i in range(len(grid)):
            row = "".join(r[i] for r in grid[::-1])
            rows.append(row)
        return rows

    def grid_rotations(self):
        zero = self.inner_grid
        once = self.rotate_grid(zero)
        twice = self.rotate_grid(once)
        thrice = self.rotate_grid(twice)

        return [
            zero, self.flip_grid(zero),
            once, self.flip_grid(once),
            twice, self.flip_grid(twice),
            thrice, self.flip_grid(thrice),
        ]


run_tests(func=get_solution, result=273)
