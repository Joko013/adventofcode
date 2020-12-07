import re

from tests import run_tests


def get_solution(puzzle_input: str):

    rules = {
        rule.split(" bags contain ")[0]: rule.split(" bags contain ")[1]
        for rule in puzzle_input.splitlines()
    }
    count = count_bags("shiny gold", rules, 1)

    return count - 1


def count_bags(name: str, rules: dict, count: int):
    total_count = count
    if name in rules:
        contained_bags = re.split(r", |\.", rules[name])[:-1]

        for bag_info in contained_bags:
            match = re.match(r"(\d+) (.+) bag", bag_info)

            if match is None:
                continue

            bag_count = int(match.group(1))
            bag_name = match.group(2)
            total_count += count * count_bags(bag_name, rules, bag_count)

    return total_count


run_tests(func=get_solution, result=126)
