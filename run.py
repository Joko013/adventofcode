from aoc import AOC
from year_19.day_03.solution_b import get_solution

aoc_data = AOC.get_data(day=3)
result = get_solution(aoc_data)
print(result)

AOC.submit(data=result, part='b', day=3)
