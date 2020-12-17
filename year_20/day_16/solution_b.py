from tests import run_tests
import re


def get_solution(puzzle_input: str):

    ticket_data = puzzle_input.split("\n\n")
    tickets = ticket_data[2].splitlines()[1:]
    my_ticket = [int(value) for value in ticket_data[1].splitlines()[1].split(",")]

    str_rules = ticket_data[0].splitlines()

    rules = dict()
    all_valid_values = set()
    for str_rule in str_rules:
        match = re.match(r"([a-z\s]+): (\d+-\d+) or (\d+-\d+)", str_rule)
        name = match.group(1)

        valid_values = set()
        for str_range in (match.group(2), match.group(3)):
            str_min, str_max = str_range.split("-")
            valid_values = valid_values.union(set(range(int(str_min), int(str_max) + 1)))
            all_valid_values = all_valid_values.union(valid_values)

        rules[name] = valid_values

    valid_tickets = [my_ticket]
    for str_ticket in tickets:
        ticket = [int(str_value) for str_value in str_ticket.split(",")]
        if all(value in all_valid_values for value in ticket):
            valid_tickets.append(ticket)

    field_positions = {name: set() for name in rules.keys()}
    for name, values in rules.items():
        for i in range(len(valid_tickets[0])):
            if all(t[i] in values for t in valid_tickets) and i not in field_positions.values():
                field_positions[name].add(i)

    while any(len(v) > 1 for v in field_positions.values()):
        for k, positions in field_positions.items():
            if len(positions) > 1:
                print(k, positions)
                for position in positions:
                    if not any(
                            position in other_positions for other, other_positions in field_positions.items() if other != k
                    ):
                        field_positions[k] = {position}
                        break

    departure_fields = set.union(*[v for k, v in field_positions.items() if "departure" in k])

    prod = 1
    for field in departure_fields:
        prod *= my_ticket[field]

    return prod


# run_tests(func=get_solution, result=71)
