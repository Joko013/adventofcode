from tests import run_tests
import re


def get_solution(puzzle_input: str):
    p1, p2 = puzzle_input.split("\n\n")
    cards_p1 = list(map(int, p1.splitlines()[1:]))
    cards_p2 = list(map(int, p2.splitlines()[1:]))

    res_p1, res_p2 = play_game(cards_p1, cards_p2)
    winning_cards = res_p1 if res_p1 else res_p2

    i = 1
    result = 0
    for card in winning_cards[::-1]:
        result += card * i
        i += 1

    return result


def play_game(cards_p1: list, cards_p2: list):
    deck_combinations = [(cards_p1, cards_p2)]
    cards_p1, cards_p2 = list(cards_p1), list(cards_p2)

    while cards_p1 and cards_p2:
        card1 = cards_p1.pop(0)
        card2 = cards_p2.pop(0)

        if len(cards_p1) >= card1 and len(cards_p2) >= card2:
            res_p1, res_p2 = play_game(cards_p1[:card1], cards_p2[:card2])
            if res_p1:
                cards_p1.append(card1)
                cards_p1.append(card2)
            else:
                cards_p2.append(card2)
                cards_p2.append(card1)

        elif card1 > card2:
            cards_p1.append(card1)
            cards_p1.append(card2)
        else:
            cards_p2.append(card2)
            cards_p2.append(card1)

        if (cards_p1, cards_p2) in deck_combinations:
            return cards_p1, list()
        else:
            deck_combinations.append((list(cards_p1), list(cards_p2)))

    return cards_p1, cards_p2


run_tests(func=get_solution, result=291)
