from tests import run_tests


def get_solution(puzzle_input: str):

    directions = puzzle_input.splitlines()
    position = complex(0, 0)
    waypoint = complex(10, 1)

    for direction in directions:
        action = direction[:1]
        value = int(direction[1:])

        if action == "N":
            waypoint += complex(0, value)

        elif action == "S":
            waypoint += complex(0, - value)

        elif action == "E":
            waypoint += complex(value, 0)

        elif action == "W":
            waypoint += complex(- value, 0)

        elif action == "R":
            waypoint *= complex(0, -1) ** (value // 90)

        elif action == "L":
            waypoint *= complex(0, 1) ** (value // 90)

        elif action == "F":
            position += value * waypoint

    return abs(position.real) + abs(position.imag)


run_tests(func=get_solution, result=286)
