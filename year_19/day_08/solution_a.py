from collections import Counter


def get_solution(inp: str):
    rows = [inp[25*n:25*(n+1)] for n in range(int(len(inp)/25))]
    layers = [rows[6*n: 6*(n+1)] for n in range(int(len(rows)/6))]

    by_zeros = sorted(layers, key=lambda x: Counter(''.join(x))['0'])
    number_of_ones = Counter(''.join(by_zeros[0]))['1']
    number_of_twos = Counter(''.join(by_zeros[0]))['2']

    return number_of_twos * number_of_ones
