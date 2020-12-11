from tests import run_tests


def get_solution(puzzle_input: str):

    seat_map = [list(line) for line in puzzle_input.splitlines()]

    offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    stop = False

    while not stop:
        next_seat_map = [list(seats) for seats in seat_map]

        for i, row in enumerate(seat_map):
            for j, seat in enumerate(row):
                occupied_neighbours = [
                    is_occupied(i + offset[0], j + offset[1], seat_map) for offset in offsets
                ]
                count_occupied_neighbours = sum(occupied_neighbours)

                if seat == "L" and count_occupied_neighbours == 0:
                    next_seat_map[i][j] = "#"
                elif seat == "#" and count_occupied_neighbours >= 4:
                    next_seat_map[i][j] = "L"

        if next_seat_map == seat_map:
            stop = True
        else:
            seat_map = next_seat_map

    return sum(row.count("#") for row in seat_map)


def is_occupied(i: int, j: int, seat_map: list):
    if i < 0 or j < 0 or i >= len(seat_map) or j >= len(seat_map[i]):
        return 0
    elif seat_map[i][j] == "#":
        return 1
    else:
        return 0


run_tests(func=get_solution, result=37)
