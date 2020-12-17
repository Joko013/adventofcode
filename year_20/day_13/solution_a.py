from tests import run_tests


def get_solution(puzzle_input: str):

    notes = puzzle_input.splitlines()
    timestamp = int(notes[0])
    bus_ids = [int(bus_id) for bus_id in notes[1].split(",") if bus_id != "x"]
    current_timestamp = timestamp

    while True:
        for bus_id in bus_ids:
            if current_timestamp % bus_id == 0:
                return (current_timestamp - timestamp) * bus_id

        current_timestamp += 1


run_tests(func=get_solution, result=295)
