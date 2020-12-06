

def get_solution(puzzle_input: str):

    answers = [group.splitlines() for group in puzzle_input.split("\n\n")]
    all_yes = [set.intersection(*(set(person) for person in group)) for group in answers]

    return sum(len(group) for group in all_yes)
