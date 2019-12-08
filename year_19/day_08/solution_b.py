
def get_solution(inp: str):
    rows = [inp[25*n:25*(n+1)] for n in range(int(len(inp)/25))]
    layers = [rows[6*n: 6*(n+1)] for n in range(int(len(rows)/6))]

    result = [['2' for i in range(26)] for j in range(6)]
    layers.reverse()
    for layer in layers:
        for i, row in enumerate(layer):
            for j, d in enumerate(row):
                if d != '2':
                    result[i][j] = d

    for r in result:
        print(''.join(str(item) if item == '1' else ' ' for item in r))

    return result
