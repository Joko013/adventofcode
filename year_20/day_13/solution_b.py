from tests import run_tests
from itertools import count


def get_solution(puzzle_input: str):
    notes = puzzle_input.splitlines()
    buses = tuple((i, int(b)) for i, b in enumerate(notes[1]) if b.isnumeric())
    n = int(notes[0])
    step = 1
    for i, b in buses:
        n = next(c for c in count(n, step) if (c + i) % b == 0)
        step *= b
        print(step, n)
    return n


run_tests(func=get_solution, result=1068781)
