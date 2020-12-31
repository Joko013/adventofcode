from tests import run_tests


def get_solution(puzzle_input: str):
    card, door = map(int, puzzle_input.splitlines())

    loop_size = get_loop_size(card)

    value = 1
    for _ in range(loop_size):
        value = (value * door) % 20201227

    return value


def get_loop_size(target):
    value = 1
    loop_size = 1

    while True:
        value = (value * 7) % 20201227

        if value == target:
            return loop_size

        loop_size += 1


run_tests(func=get_solution, result=10)
