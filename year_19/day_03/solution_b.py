

def get_solution(inp: str):
    """Where do the wires intersect? Which one can be reached in the least amount of steps?"""
    wires = [[wire for wire in wire_str.split(',')] for wire_str in inp.split('\n')]

    paths = list()
    for wire in wires:
        # current of the wire on the grid (always start at [0, 0])
        # position[0] is X ~> left-right position
        # position[1] is Y ~> up-down position
        position = [0, 0]
        points = list()

        for step in wire:
            # first position in the string is always the direction of the step
            direction = step[0]
            # second is the amount of steps
            steps = int(step[1:])

            for _ in range(steps):
                if direction == 'R':
                    position[0] += 1
                elif direction == 'L':
                    position[0] -= 1
                elif direction == 'U':
                    position[1] += 1
                elif direction == 'D':
                    position[1] -= 1

                points.append(position[:])

        paths.append(points[:])

    # get only unique points so intersect
    unique_points = [set(tuple(point) for point in path) for path in paths]
    intersections = unique_points[0] & unique_points[1]

    step_sums = list()
    # get sum of steps for each intersection
    for i in intersections:
        i_l = list(i)

        steps_w1 = paths[0].index(i_l) + 1
        steps_w2 = paths[1].index(i_l) + 1
        step_sums.append(steps_w1 + steps_w2)

    return min(step_sums)
