from tests import run_tests


def get_solution(puzzle_input: str):

    current_state = [puzzle_input.splitlines()]

    for _ in range(6):
        wrapped = wrap_state(current_state)

        new_state = []
        for i, layer in enumerate(wrapped):
            new_layer = []
            for j, row in enumerate(layer):
                new_row = ""

                for k in range(len(row)):
                    active_neighbours = count_active(i, j, k, wrapped)

                    if wrapped[i][j][k] == "#" and active_neighbours in {2, 3}:
                        new_row += "#"
                    elif wrapped[i][j][k] == "." and active_neighbours == 3:
                        new_row += "#"
                    else:
                        new_row += "."

                new_layer.append(new_row)

            new_state.append(new_layer)

        current_state = new_state

    return sum(sum(row.count("#") for row in layer) for layer in current_state)


def count_active(i: int, j: int, k: int, state: list):
    neighbours = [
        (i - a, j - b, k - c)
        for a in (-1, 0, 1)
        for b in (-1, 0, 1)
        for c in (-1, 0, 1)
    ]
    neighbours.pop(neighbours.index((i, j, k)))

    active_count = 0
    for neighbour in neighbours:

        n_i, n_j, n_k = neighbour[0], neighbour[1], neighbour[2]
        if (n_i < 0 or n_i >= len(state)) or \
                (n_j < 0 or n_j >= len(state[0])) or \
                (n_k < 0 or n_k >= len(state[0][0])):
            continue

        else:
            if state[n_i][n_j][n_k] == "#":
                active_count += 1

    return active_count


def wrap_layer(layer: list):
    wrapped_inner = ["." + row + "." for row in layer]
    wrapped_inner.insert(0, "." * len(wrapped_inner[0]))
    wrapped_inner.append("." * len(wrapped_inner[0]))

    return wrapped_inner


def wrap_state(state: list):
    wrapped = []
    for layer in state:
        wrapped.append(wrap_layer(layer))

    empty_layer = ["." * len(wrapped[0][0]) for _ in range(len(wrapped[0]))]
    wrapped.insert(0, empty_layer)
    wrapped.append(empty_layer)

    return wrapped


run_tests(func=get_solution, result=112)
