from tests import run_tests


def get_solution(puzzle_input: str):
    notes = puzzle_input.splitlines()
    buses = [(i, int(b)) for i, b in enumerate(notes[1].split(",")) if b.isnumeric()]
    timestamp = int(notes[0])
    step = 1
    for i, b in buses:
        while (timestamp + i) % b != 0:
            timestamp += step

        step *= b

    return timestamp


run_tests(func=get_solution, result=1068781)
