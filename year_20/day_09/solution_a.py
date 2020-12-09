from tests import run_tests


def get_solution(puzzle_input: str):

    series = [int(line) for line in puzzle_input.splitlines()]

    for i in range(len(series)):

        number = series[25 + i]
        previous_numbers = set(series[i: 25 + i])

        if not any((number - other) in previous_numbers for other in previous_numbers):
            return number


# run_tests(func=get_solution, result=127)
