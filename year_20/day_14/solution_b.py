from tests import run_tests
from itertools import count


def get_solution(puzzle_input: str):
    lines = [line.split(" = ") for line in puzzle_input.splitlines()]
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = dict()

    for line in lines:

        if line[0] == "mask":
            mask = line[1]
        else:
            address = int(line[0][4:-1])
            value = int(line[1])

            binary_address = f"{address:036b}"
            addresses = {binary_address}

            for i, char in enumerate(mask):
                if char == "1":
                    addresses = {a[:i] + "1" + a[i + 1:] for a in addresses}

                elif char == "X":
                    address_combinations = set()
                    for item in ("0", "1"):
                        address_combinations = address_combinations.union({a[:i] + item + a[i + 1:] for a in addresses})

                    addresses = addresses.union(address_combinations)

            for address in addresses:
                memory[address] = value

    return sum(memory.values())


run_tests(func=get_solution, result=208)
