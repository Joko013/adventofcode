from aoc import AOC
from year_19.day_04.solution_b import get_solution

aoc_data = AOC.get_data(day=4)
result = get_solution(aoc_data)
print(result)

AOC.submit(data=len(result), part='b', day=4)
