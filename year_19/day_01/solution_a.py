from aoc import AOC


def get_solution(inp: str):
    mass_data = [int(item) for item in inp.split('\n')]
    fuel_data = [(mass // 3) - 2 for mass in mass_data]
    total_fuel = sum(fuel_data)
    return total_fuel


aoc_data = AOC.get_data(1)
result = get_solution(aoc_data)

AOC.submit(data=result, part='a', day=1)
