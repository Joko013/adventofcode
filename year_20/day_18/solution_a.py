from tests import run_tests


def get_solution(puzzle_input: str):
    lines = puzzle_input.splitlines()

    return sum(solve(line) for line in lines)


def solve(line: str) -> int:
    result = 0
    operation = "+"
    skip = 0

    for i, char in enumerate(line):
        if char == " ":
            continue

        if skip:
            if char == "(":
                skip += 1
            if char == ")":
                skip -= 1
            continue

        if char in {"+", "*"}:
            operation = char

        elif char == "(":
            value = solve(line[i + 1:])
            result = evaluate(result, value, operation)
            skip += 1

        elif char == ")":
            return result

        else:
            value = int(char)
            result = evaluate(result, value, operation)

    return result


def evaluate(num1: int, num2: int, operation: str):
    if operation == "*":
        return num1 * num2
    else:
        return num1 + num2


run_tests(func=get_solution, result=26)
