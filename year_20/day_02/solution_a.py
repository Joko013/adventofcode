
def get_solution(puzzle_input: str):

    entries = puzzle_input.split("\n")
    correct_passwords = 0

    for entry in entries:
        sliced_entry = entry.split(" ")

        counts = sliced_entry[0].split("-")
        min_count, max_count = int(counts[0]), int(counts[1])

        char = sliced_entry[1].replace(":", "")
        password = sliced_entry[2]

        if max_count >= password.count(char) >= min_count:
            correct_passwords += 1

    return correct_passwords
