import numpy


def get_solution(puzzle_input: str):

    rows = puzzle_input.split("\n")
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    slope_tress = [get_trees(rows, slope[0], slope[1]) for slope in slopes]

    return numpy.prod(slope_tress, dtype=numpy.int64)


def get_trees(rows: list, x_offset: int, y_offset: int):
    trees = 0
    index = 0

    for i, row in enumerate(rows):
        if i % y_offset == 0:
            position = row[index % len(row)]

            if position == "#":
                trees += 1

            index += x_offset

    return trees
