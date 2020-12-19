from tests import run_tests
import re


def get_solution(puzzle_input: str):
    rules_str, messages_str = puzzle_input.split("\n\n")
    rules = {rule.split(": ")[0]: rule.split(": ")[1] for rule in rules_str.splitlines()}
    messages = messages_str.splitlines()

    pattern = eval_rule("0", rules) + "\Z"
    sum_ = sum(bool(re.match(pattern, message)) for message in messages)
    return sum_


def eval_rule(rule_index: str, rules: dict) -> str:
    rule = rules[rule_index]

    if rule_index == "8":
        return eval_rule("42", rules) + "+"
    elif rule_index == "11":
        r42 = eval_rule("42", rules)
        r31 = eval_rule("31", rules)
        return "(" + "|".join(f"{r42}{{{n}}}{r31}{{{n}}}" for n in range(1, 50)) + ")"

    if rule.startswith("\""):
        return rule.replace("\"", "")
    else:
        parts = rule.split(" | ")

        re_parts = []
        for part in parts:
            numbers = part.split(" ")
            part_result = ""
            for number in numbers:
                part_result += eval_rule(number, rules)
            re_parts.append(part_result)

        result = "(" + "|".join(re_part for re_part in re_parts) + ")"
        return result


run_tests(func=get_solution, result=2)
