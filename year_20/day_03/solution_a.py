
def get_solution(puzzle_input: str):

    rows = puzzle_input.split("\n")

    trees = 0
    index = 0

    for row in rows:
        position = row[index % len(row)]

        if position == "#":
            trees += 1

        index += 3

    return trees
