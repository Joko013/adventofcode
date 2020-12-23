from tests import run_tests


def get_solution(puzzle_input: str):
    cups = list(map(int, puzzle_input))

    for _ in range(100):
        current_cup = cups[0]
        three_cups = [cups.pop(1), cups.pop(1), cups.pop(1)]

        try:
            diff = min(current_cup - cup for cup in cups if current_cup - cup > 0)
            destination_cup = current_cup - diff
        except ValueError:
            destination_cup = max(cups)

        destination_index = cups.index(destination_cup)
        cups = cups[:destination_index + 1] + three_cups + cups[destination_index + 1:]
        cups = cups[1:] + cups[:1]

    return "".join(map(str, cups[cups.index(1) + 1:] + cups[:cups.index(1)]))


run_tests(func=get_solution, result="67384529")
