from tests import run_tests


def get_solution(puzzle_input: str):

    adapters = [int(line) for line in puzzle_input.splitlines()]
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)

    differences = {1: 0, 2: 0, 3: 0}
    for i in range(len(adapters) - 1):
        differences[adapters[i + 1] - adapters[i]] += 1

    return differences[1] * differences[3]


run_tests(func=get_solution, result=35)
