
def get_solution(inp: str):

    complements = dict()
    for entry in inp.split('\n'):
        entry = int(entry)

        for k, v in complements.items():
            if entry in v:
                return k * entry * (2020 - k - entry)
            else:
                v.add(2020 - k - entry)

        complements[entry] = set()
