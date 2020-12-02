
def get_solution(puzzle_input: str):

    entries = puzzle_input.split("\n")
    correct_passwords = 0

    for entry in entries:
        sliced_entry = entry.split(" ")

        positions = sliced_entry[0].split("-")
        position_1, position_2 = int(positions[0]) - 1, int(positions[1]) - 1

        char = sliced_entry[1].replace(":", "")
        password = sliced_entry[2]

        if (
                password[position_1] == char and not password[position_2] == char
        ) or (
                password[position_2] == char and not password[position_1] == char
        ):
            correct_passwords += 1

    return correct_passwords
