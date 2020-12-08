from tests import run_tests


def get_solution(puzzle_input: str):

    instructions = puzzle_input.splitlines()
    i = 0
    accumulator = 0
    visited_instructions = set()

    while True:
        if i in visited_instructions:
            return accumulator
        else:
            visited_instructions.add(i)

        instruction = instructions[i]
        operation, argument = instruction.split(" ")

        if operation == "acc":
            accumulator += int(argument)
            i += 1
        elif operation == "jmp":
            i += int(argument)
        elif operation == "nop":
            i += 1


run_tests(func=get_solution, result=5)
