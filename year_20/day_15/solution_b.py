from tests import run_tests


def get_solution(puzzle_input: str):

    numbers = [int(num) for num in puzzle_input.split(",")]
    indices = {num: [i] for i, num in enumerate(numbers)}
    last_number = numbers[-1]

    for i in range(len(numbers), 30000000):
        num_indices = indices[last_number]

        if len(num_indices) > 1:
            new_number = num_indices[-1] - num_indices[-2]
        else:
            new_number = 0

        if new_number in indices:
            indices[new_number].append(i)
        else:
            indices[new_number] = [i]

        last_number = new_number

    return last_number


run_tests(func=get_solution, result=362)
