
def get_solution(puzzle_input: str):

    boarding_passes = puzzle_input.split("\n")

    seat_ids = set()

    for boarding_pass in boarding_passes:
        seat_id = int(boarding_pass.replace('F', "0").replace("B", "1").replace("R", "1").replace("L", "0"), base=2)
        seat_ids.add(seat_id)

    for id_ in seat_ids:
        if (id_ + 2 in seat_ids) and (id_ + 1 not in seat_ids):
            return id_ + 1
