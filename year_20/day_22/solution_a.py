from tests import run_tests
import re


def get_solution(puzzle_input: str):
    p1, p2 = puzzle_input.split("\n\n")
    cards_p1 = list(map(int, p1.splitlines()[1:]))
    cards_p2 = list(map(int, p2.splitlines()[1:]))

    while cards_p1 and cards_p2:

        card1 = cards_p1.pop(0)
        card2 = cards_p2.pop(0)

        if card1 > card2:
            cards_p1.append(card1)
            cards_p1.append(card2)
        else:
            cards_p2.append(card2)
            cards_p2.append(card1)

    winning_cards = cards_p1 if cards_p1 else cards_p2

    i = 1
    result = 0
    for card in winning_cards[::-1]:
        result += card * i
        i += 1

    return result


run_tests(func=get_solution, result=306)
