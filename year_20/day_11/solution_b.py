from tests import run_tests


def get_solution(puzzle_input: str):

    seat_map = [list(line) for line in puzzle_input.splitlines()]

    directions = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
    ]

    while True:
        next_seat_map = [list(seats) for seats in seat_map]

        for i, row in enumerate(seat_map):
            for j, seat in enumerate(row):
                neighbours_occupied = [
                    is_occupied(i, j, seat_map, direction) for direction in directions
                ]
                count_occupied_neighbours = sum(neighbours_occupied)

                if seat == "L" and count_occupied_neighbours == 0:
                    next_seat_map[i][j] = "#"
                elif seat == "#" and count_occupied_neighbours >= 5:
                    next_seat_map[i][j] = "L"

        if next_seat_map == seat_map:
            break
        else:
            seat_map = next_seat_map

    return sum(row.count("#") for row in seat_map)


def is_occupied(i: int, j: int, seat_map: list, direction: tuple):
    i, j = i + direction[0], j + direction[1]
    if i < 0 or j < 0 or i >= len(seat_map) or j >= len(seat_map[i]):
        return False
    elif seat_map[i][j] == ".":
        return is_occupied(i, j, seat_map, direction)
    elif seat_map[i][j] == "#":
        return True
    else:
        return False


run_tests(func=get_solution, result=26)
