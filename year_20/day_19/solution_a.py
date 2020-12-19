from tests import run_tests
import re


def get_solution(puzzle_input: str):
    rules_str, messages_str = puzzle_input.split("\n\n")
    rules = {rule.split(": ")[0]: rule.split(": ")[1].split(" ") for rule in rules_str.splitlines()}
    messages = messages_str.splitlines()

    pattern = eval_rule(rules["0"], rules)
    return sum(bool(re.match(f"{pattern}\Z", message)) for message in messages)


def eval_rule(rule: str, rules: dict) -> str:
    if rule[0].startswith("\""):
        result = rule[0].replace("\"", "")
    else:
        result = ""
        for char in rule:
            if char.isnumeric():
                result += eval_rule(rules[char], rules)
            else:
                result += char
        result = "(" + result + ")"

    return result


run_tests(func=get_solution, result=2)
