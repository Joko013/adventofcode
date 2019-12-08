
def get_solution(inp: str):

    orbit_map = [tuple(item.split(')')) for item in inp.split('\n')]

    # orbit_map = [
    #     ('COM', 'b'), ('b', 'g'), ('g', 'h'), ('b', 'c'), ('c', 'd'), ('d', 'i'), ('d', 'e'), ('e', 'f'), ('e', 'j'),
    #     ('j', 'k'), ('k', 'l')
    # ]
    orbit_map_ = orbit_map[:]

    new_map = [['COM']]
    i = 0

    while orbit_map:
        for j, orbit in enumerate(orbit_map):
            base = orbit[0]
            orbiter = orbit[1]
            for item in new_map:
                try:
                    if item[i] == base:
                        if len(item) > i + 1:
                            new_ = item[:-1]
                            new_.append(orbiter)
                            new_map.append(new_)
                        else:
                            item.append(orbiter)
                        orbit_map_.pop(orbit_map_.index(orbit))
                        break
                except IndexError:
                    pass
        i += 1
        orbit_map = orbit_map_[:]

    planet_distances = dict()
    for path in new_map:
        for i, planet in enumerate(path):
            planet_distances[planet] = i

    total_distance = sum(v for (k, v) in planet_distances.items())
    return total_distance
