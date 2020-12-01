from aoc import AOC
from year_20.day_01.solution_b import get_solution

aoc_data = AOC.get_data(day=1, year=2020)
result = get_solution(aoc_data)
# print(result)

AOC.submit(data=result, part='b', day=1, year=2020)
