from tests import run_tests
import re


def get_solution(puzzle_input: str):

    ticket_data = puzzle_input.split("\n\n")
    tickets = ticket_data[2].splitlines()[1:]
    validity_ranges = re.findall(r"(\d+-\d+) or (\d+-\d+)", ticket_data[0])

    valid_values = set()
    for pair in validity_ranges:
        for str_range in pair:
            str_min, str_max = str_range.split("-")
            valid_values = valid_values.union(set(range(int(str_min), int(str_max) + 1)))

    invalid_values = []
    for ticket in tickets:
        for str_value in ticket.split(","):
            value = int(str_value)

            if value not in valid_values:
                invalid_values.append(value)

    return sum(invalid_values)


run_tests(func=get_solution, result=71)
