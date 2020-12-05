import math


def get_solution(puzzle_input: str):

    boarding_passes = puzzle_input.split("\n")
    max_id = 0

    for boarding_pass in boarding_passes:

        min_row, max_row = 0, 127
        for char in boarding_pass[:7]:
            offset = math.ceil((max_row - min_row) / 2)
            if char == "F":
                max_row -= offset
            else:
                min_row += offset

        min_seat, max_seat = 0, 7
        for char in boarding_pass[7:]:
            offset = math.ceil((max_seat - min_seat) / 2)
            if char == "L":
                max_seat -= offset
            else:
                min_seat += offset

        seat_id = max_row * 8 + max_seat
        # apparently it's a binary number if you just convert it to 0s and 1s
        # seat_id = int(boarding_pass.replace('F',"0").replace("B","1").replace("R","1").replace("L","0"), base=2)

        if seat_id > max_id:
            max_id = seat_id

    return max_id
