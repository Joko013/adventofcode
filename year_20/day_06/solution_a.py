
def get_solution(puzzle_input: str):

    answers = [set(group.replace("\n", "")) for group in puzzle_input.split("\n\n")]

    return sum(len(group) for group in answers)
