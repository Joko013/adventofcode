from tests import run_tests
import re


def get_solution(puzzle_input: str):
    lines = [line.split(" (contains ") for line in puzzle_input.splitlines()]
    ingredients = [{i for i in line[0].split(" ")} for line in lines]
    allergens = [{a for a in line[1][:-1].split(", ")} for line in lines]

    options = dict()
    for allergen in set.union(*allergens):
        for i in range(len(ingredients)):
            if allergen not in allergens[i]:
                continue

            if options.get(allergen) is None:
                options[allergen] = ingredients[i]
            else:
                options[allergen] = options[allergen].intersection(ingredients[i])

    while any(len(value) > 1 for value in options.values()):
        for allergen, possibilities in options.items():
            if len(possibilities) == 1:
                continue

            new_possibilities = set()
            for possibility in possibilities:
                if any(possibility in val and len(val) == 1 for val in options.values()):
                    continue
                else:
                    new_possibilities.add(possibility)

            options[allergen] = new_possibilities

    result = ""
    for allergen, ingredient in sorted(options.items()):
        result += ingredient.pop() + ","

    return result[:-1]


run_tests(func=get_solution, result="mxmxvkd,sqjhc,fvjkl")
