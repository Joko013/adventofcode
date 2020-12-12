from tests import run_tests


def get_solution(puzzle_input: str):

    directions = puzzle_input.splitlines()

    orientation = "E"
    position = {"N": 0, "S": 0, "E": 0, "W": 0}
    orientations = ["E", "S", "W", "N"]

    for direction in directions:
        action = direction[:1]
        value = int(direction[1:])

        if action == "F":
            position[orientation] += value
        elif action in {"R", "L"}:
            index = orientations.index(orientation)
            offset = value // 90
            new_index = int((index + offset) % 4) if action == "R" else int((index - offset) % 4)
            orientation = orientations[new_index]
        else:
            position[action] += value

    return abs(position["N"] - position["S"]) + abs(position["E"] - position["W"])


run_tests(func=get_solution, result=25)
