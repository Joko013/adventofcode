from tests import run_tests


def get_solution(puzzle_input: str):

    numbers = [int(num) for num in puzzle_input.split(",")]
    print(numbers)

    for i in range(len(numbers), 2020):
        last = numbers[-1]

        numbers_before = numbers[:i - 1]
        if last in numbers_before:
            numbers_before.reverse()
            previous_occurrence = numbers_before.index(last)
            numbers.append(previous_occurrence + 1)

        else:
            numbers.append(0)

    print(numbers[2019])
    return numbers[2019]


run_tests(func=get_solution, result=1836)
