
def get_solution(inp: str):

    complements = set()
    for entry in inp.split('\n'):
        entry = int(entry)

        if entry in complements:
            return entry * (2020 - entry)
        else:
            complements.add(2020 - entry)
