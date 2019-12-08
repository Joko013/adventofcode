
def get_solution(inp: str):

    orbit_map = [tuple(item.split(')')) for item in inp.split('\n')]

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

    for path in new_map:
        if 'YOU' in path:
            you_path = path[:-1]
        elif 'SAN' in path:
            san_path = path[:-1]

    for i, item in enumerate(you_path):
        if item in san_path:
            continue
        else:
            you_len = len(you_path[i:])
            san_len = len(san_path[i:])
            break

    return you_len + san_len
