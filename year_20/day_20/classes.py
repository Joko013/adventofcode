from __future__ import annotations
from typing import Optional, Tuple


class Tile:
    def __init__(self, rows: list, tile_id: str):
        self.rows = rows
        self.tile_id = tile_id

    def __repr__(self):
        return f"Tile: {self.tile_id}"

    def row(self, i) -> str:
        return self.rows[i]

    def column(self, i) -> str:
        return "".join(row[i] for row in self.rows)

    def flip(self) -> Tile:
        return Tile([row[::-1] for row in self.rows], self.tile_id)

    def rotate_clockwise(self) -> Tile:
        rows = []
        for i in range(len(self.rows)):
            row = "".join(r[i] for r in self.rows[::-1])
            rows.append(row)
        return Tile(rows, self.tile_id)

    def borders_side(self, other: Tile) -> Optional[str]:
        side = None
        if self.row(0) == other.row(9):
            side = "up"
        elif self.row(9) == other.row(0):
            side = "down"
        elif self.column(9) == other.column(0):
            side = "right"
        elif self.column(0) == other.column(9):
            side = "left"

        return side

    @property
    def all_rotations(self):
        base = self
        once = self.rotate_clockwise()
        twice = once.rotate_clockwise()
        thrice = twice.rotate_clockwise()

        return [
            base, base.flip(), once, once.flip(), twice, twice.flip(), thrice, thrice.flip()
        ]

    def borders(self, other: Tile) -> Optional[Tuple[str, Tile]]:
        for other_rotation in other.all_rotations:
            borders_side = self.borders_side(other_rotation)
            if borders_side:
                return borders_side, other_rotation

    def neighbours(self, other_tiles):
        neighbours = dict()

        for other_id, other in other_tiles.items():
            if other is self:
                continue

            borders = self.borders(other)
            if borders:
                border, tile = borders
                neighbours[border] = tile

        return neighbours

    def __str__(self):
        return "\n".join(row for row in self.rows)

    @property
    def inner(self) -> Tile:
        tiles = [self.rows[i][1:len(self.rows[i]) - 1] for i in range(1, len(self.rows) - 1)]
        return Tile(tiles, self.tile_id)
