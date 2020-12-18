from tests import run_tests
import re


def get_solution(puzzle_input: str):
    lines = puzzle_input.splitlines()
    return sum(int(reduce(line)) for line in lines)


def reduce(line: str):
    while " " in line:
        # first reduce (...)
        parentheses_match = re.search(r"\(.+?\)", line)
        if parentheses_match:
            start = parentheses_match.span()[0]

            # the regex matches only the first ), so in case of nested (...(...)...)
            # find the real closing )
            if parentheses_match[0].count("(") != parentheses_match[0].count(")"):
                end = find_closing_parenthesis(line, start)
            else:
                end = parentheses_match.span()[1]

            value = reduce(line[start + 1:end - 1])

        # then evaluate + and finally *
        else:
            match = re.search(r"\d+ \+ \d+", line) or re.search(r"\d+ \* \d+", line)
            value = str(eval(match[0]))
            start, end = match.span()[0], match.span()[1]

        line = line[:start] + value + line[end:]

    return line


def find_closing_parenthesis(line, start):
    opening, closing = 0, 0
    for i, char in enumerate(line[start:]):
        if char == "(":
            opening += 1
        elif char == ")":
            closing += 1

        if opening == closing:
            return start + i + 1


run_tests(func=get_solution, result=669060)
