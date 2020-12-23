from tests import run_tests


class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Cup: {self.value}"


def get_solution(puzzle_input: str):
    cups = list(map(int, puzzle_input))
    number_of_cups = 10 ** 6
    number_of_steps = 10 ** 7

    # a cup on each position
    lookup_table = {i: Cup(i) for i in range(1, number_of_cups + 1)}

    # last cup points back to first
    lookup_table[number_of_cups].next = lookup_table[cups[0]]
    # every cup points to the next in line
    for i in range(1, number_of_cups):
        lookup_table[i].next = lookup_table[i + 1]

    # adjust first n cups based on the input cup order
    lookup_table[cups[-1]].next = lookup_table[len(cups) + 1]
    for i, value in enumerate(cups[:-1]):
        lookup_table[value].next = lookup_table[cups[i + 1]]

    current_cup = lookup_table[cups[0]]

    for _ in range(number_of_steps):
        next1, next2, next3 = current_cup.next, current_cup.next.next, current_cup.next.next.next
        # take out the next 3 cups
        current_cup.next = next3.next

        # find where to move the 3 cups
        destination_cup_value = current_cup.value - 1 if current_cup.value > 1 else number_of_cups
        while destination_cup_value in {next1.value, next2.value, next3.value}:
            destination_cup_value -= 1
            if destination_cup_value < 1:
                destination_cup_value = number_of_cups

        # move the 3 cups
        destination_cup = lookup_table[destination_cup_value]
        next3.next = destination_cup.next
        destination_cup.next = next1
        # go to next cup
        current_cup = current_cup.next

    return lookup_table[1].next.value * lookup_table[1].next.next.value


run_tests(func=get_solution, result=149245887792)
