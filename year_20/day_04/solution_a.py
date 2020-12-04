
def get_solution(puzzle_input: str):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    passport_data = [row.replace("\n", " ") for row in puzzle_input.split("\n\n")]
    passports = [dict(field.split(":") for field in passport_str.split(" ")) for passport_str in passport_data]

    valid_passports = 0
    for passport in passports:
        if all(field in passport for field in required_fields):
            valid_passports += 1

    return valid_passports
