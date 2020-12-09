from tests import run_tests


def get_solution(puzzle_input: str):

    series = [int(line) for line in puzzle_input.splitlines()]
    number, number_index = find_error(series)

    # for each subset of j numbers
    for j in range(2, len(series[:number_index])):

        # for each position of the subset in the series
        for k in range(len(series[:number_index]) - j):
            sub_series = series[k: k + j]

            if sum(sub_series) == number:
                return min(sub_series) + max(sub_series)


def find_error(series: list):
    for i in range(len(series)):

        number_index = 25 + i
        number = series[number_index]
        previous_numbers = set(series[i: number_index])

        if not any((number - other) in previous_numbers for other in previous_numbers):
            return number, number_index

# run_tests(func=get_solution, result=62)
