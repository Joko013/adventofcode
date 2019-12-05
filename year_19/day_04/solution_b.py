

def get_solution(inp: str):
    range_ = [int(item) for item in inp.split('-')]

    valid_nums = list()
    for num in range(range_[0], range_[1]+1):
        is_valid = test_number(num)
        if is_valid:
            valid_nums.append(num)

    return len(valid_nums)


def test_number(num: int):
    num_str = str(num)

    # the digits never decrease
    digit_pairs = list()
    for d in range(1, len(num_str)):
        if num_str[d] < num_str[d-1]:
            return False

        pair = (num_str[d-1], num_str[d])
        digit_pairs.append(pair)

    # there is a pair consisting of two of the same digit
    same_digit_pairs = [item for item in digit_pairs if item[0] == item[1]]
    if not same_digit_pairs:
        return False

    # there is a digit pair that is not a part of a digit trio
    digit_trios = [(num_str[d-2], num_str[d-1], num_str[d]) for d in range(2, len(num_str))]
    same_digit_trios = [trio for trio in digit_trios if trio[0] == trio[1] == trio[2]]
    any_single_pair = any(True for pair in same_digit_pairs if all(pair[0] not in trio for trio in same_digit_trios))
    if not any_single_pair:
        return False

    return True
