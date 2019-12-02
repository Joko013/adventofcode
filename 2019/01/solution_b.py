from aoc import AOC


def get_solution(inp: str):
    mass_data = [int(item) for item in inp.split('\n')]

    fuel_data = []
    for mass in mass_data:
        # fuel required for the module
        fuel = get_fuel(mass)

        # fuel required for the fuel itself
        while fuel > 0:
            fuel_data.append(fuel)
            fuel = get_fuel(fuel)

    total_fuel = sum(fuel_data)
    return total_fuel


def get_fuel(mass: int):
    return mass // 3 - 2


aoc_data = AOC.get_data(1)
result = get_solution(aoc_data)
print(result)

# AOC.submit(data=result, part='b', day=1)
