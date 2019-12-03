from aoc import AOC
from year_19.day_03.solution_a import get_solution

aoc_data = AOC.get_data(day=3)
result = get_solution(aoc_data)
print(result)

AOC.submit(data=result, part='a', day=3)
