

def get_solution(inp: str):
    """Where do the wires intersect? Which is the closest to the start?"""
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
                    points.append(position[:])
                elif direction == 'L':
                    position[0] -= 1
                    points.append(position[:])
                elif direction == 'U':
                    position[1] += 1
                    points.append(position[:])
                elif direction == 'D':
                    position[1] -= 1
                    points.append(position[:])

        # get only unique points for each wire
        unique_points = set(tuple(point) for point in points)
        paths.append(unique_points)

    intersections = paths[0] & paths[1]

    # calculate distances based on absolute distance from the origin
    distances = list()
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        distances.append(dist)

    return min(distances)

