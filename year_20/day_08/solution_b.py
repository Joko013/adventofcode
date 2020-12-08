from typing import Optional
from tests import run_tests


def get_solution(puzzle_input: str):

    instructions = puzzle_input.splitlines()

    for i, instruction in enumerate(instructions):
        test_instructions = list(instructions)
        if "nop" in instruction:
            test_instructions[i] = instructions[i].replace("nop", "jmp")
        elif "jmp" in instruction:
            test_instructions[i] = instructions[i].replace("jmp", "nop")

        result = run_instruction(test_instructions)
        if result is not None:
            return result


def run_instruction(instructions: list) -> Optional[int]:
    i = 0
    accumulator = 0
    visited_instructions = set()

    while True:
        if i >= len(instructions):
            return accumulator
        elif i in visited_instructions:
            return None

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


run_tests(func=get_solution, result=8)
