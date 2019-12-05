

def get_solution(inp: str):
    range_ = [int(item) for item in inp.split('-')]

    valid_nums = list()
    for num in range(range_[0], range_[1]+1):
        is_valid = test_number(num)
        if is_valid:
            valid_nums.append(num)

    return len(valid_nums)


def test_number(num: int) -> bool:
    num_str = str(num)

    digit_pairs = list()
    for d in range(1, len(num_str)):
        if num_str[d] < num_str[d-1]:
            return False

        pair = (num_str[d-1], num_str[d])
        digit_pairs.append(pair)

    has_same_digit_pair = any(item[0] == item[1] for item in digit_pairs)
    if not has_same_digit_pair:
        return False

    return True
