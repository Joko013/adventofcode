

def get_solution(inp: str):
    range_ = [int(item) for item in inp.split('-')]

    valid_nums = list()
    for num in range(range_[0], range_[1]+1):
        valid_num = get_valid_number(num)
        if valid_num:
            valid_nums.append(valid_num)

    return valid_nums


def get_valid_number(num: int):
    num_str = str(num)

    digit_pairs = list()
    for d in range(1, len(num_str)):
        if num_str[d] < num_str[d-1]:
            return

        pair = (num_str[d-1], num_str[d])
        digit_pairs.append(pair)

    has_same_digit_pair = any(item[0] == item[1] for item in digit_pairs)
    if not has_same_digit_pair:
        return

    return num
