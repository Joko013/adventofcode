from tests import run_tests


def get_solution(puzzle_input: str):

    rules = [rule.split(" bags contain ") for rule in puzzle_input.splitlines()]
    bags = make_bags("shiny gold", rules)

    return len(bags) - 1


def make_bags(name: str, rules: list):
    bags = {name}
    for rule in rules:
        bag_name, contains = rule[0], rule[1]

        if name in contains:
            bags = bags.union(make_bags(bag_name, rules))

    return bags


run_tests(func=get_solution, result=4)
