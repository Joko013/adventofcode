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

    no_allergen = []
    for recipe in ingredients:
        for item in recipe:
            if not any(item in option for option in options.values()):
                no_allergen.append(item)

    return len(no_allergen)


run_tests(func=get_solution, result=5)
