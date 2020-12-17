from aoc import AOC
from year_20.day_17.solution_b import get_solution

day = 17
part = "b"

aoc_data = AOC.get_data(day=day, year=2020)
result = get_solution(aoc_data)
print(result)
# AOC.submit(data=result, part=part, day=day, year=2020)
