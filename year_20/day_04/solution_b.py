
import re


def get_solution(puzzle_input: str):
    field_rules = {
        "byr": r"\A(19[2-9][0-9])|(200[0-2])\Z",
        "iyr": r"\A(201[0-9])|(2020)\Z",
        "eyr": r"\A(202[0-9])|(2030)\Z",
        "hgt": r"\A(1([5-8][0-9]|[9][0-3])cm)|((59|6[0-9]|7[0-6])in)\Z",
        "hcl": r"\A#[a-f0-9]{6}\Z",
        "ecl": r"\A(amb|blu|brn|gry|grn|hzl|oth)\Z",
        "pid": r"\A\d{9}\Z",
    }

    passport_data = [row.replace("\n", " ") for row in puzzle_input.split("\n\n")]
    passports = [dict(field.split(":") for field in passport_str.split(" ")) for passport_str in passport_data]

    valid_passports = 0
    for passport in passports:
        if all(re.match(rule, passport.get(field, "")) for field, rule in field_rules.items()):
            valid_passports += 1

    return valid_passports
