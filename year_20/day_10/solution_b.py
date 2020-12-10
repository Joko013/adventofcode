from tests import run_tests


def get_solution(puzzle_input: str):

    adapters = [int(line) for line in puzzle_input.splitlines()]
    adapters.sort()

    combinations = {0: 1}
    for jolts in adapters:
        combinations[jolts] = combinations.get(jolts - 1, 0) \
                              + combinations.get(jolts - 2, 0) \
                              + combinations.get(jolts - 3, 0)

    return combinations[adapters[-1]]


run_tests(func=get_solution, result=8)
