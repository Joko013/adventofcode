from tests import run_tests


def get_solution(puzzle_input: str):

    lines = [line.split(" = ") for line in puzzle_input.splitlines()]
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = dict()

    for line in lines:

        if line[0] == "mask":
            mask = line[1]
        else:
            address = line[0][4:-1]
            value = int(line[1])
            binary = f"{value:036b}"

            for i, char in enumerate(mask):
                if char != "X":
                    binary = binary[:i] + char + binary[i + 1:]

            memory[address] = int(binary, 2)

    return sum(memory.values())


run_tests(func=get_solution, result=165)
