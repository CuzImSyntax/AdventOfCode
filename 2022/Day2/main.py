from typing import Dict, List

# Rock      = 1
# Paper     = 2
# Scissors  = 3

#Convert the input into a number to make comparing easier
input_dict: Dict[str, int] = {"A": 1, "B": 2, "C": 3,
                              "X": 1, "Y": 2, "Z": 3}

#Compare the second input to amount to be added
winning_dict: Dict[str, int] = {"X": 0, "Y": 3, "Z": 6}

def get_data() -> List[List[str]]:
    with open("input.txt", "r") as file:
        lines: List[List[str]] = [line.split(" ") for line in file.read().split("\n")]
    return lines

def evaluate_game(first: int, second: int) -> int:
    if first == second:
        return 3

    if (first == 1 and second == 2) or (first == 2 and second == 3) or (first == 3 and second == 1):
        return 6

    return 0


def part_one() -> int:
    sum_: int = 0
    data: List[List[str]] = get_data()
    for game in data:
        sum_ += evaluate_game(input_dict[game[0]], input_dict[game[1]])
        sum_+= input_dict[game[1]]

    return sum_

def calculate_figure(first: int, second: int) -> int:
    if second == 1:
        return (first-1) if first > 1 else 3
    elif second == 3:
        return (first+1) if first < 3 else 1
    return first


def part_two() -> int:
    sum_: int = 0
    data: List[List[str]] = get_data()
    for game in data:
        sum_ += winning_dict[game[1]]
        sum_ += calculate_figure(input_dict[game[0]], input_dict[game[1]])

    return sum_

if __name__ == "__main__":
    print(part_one())
    print(part_two())
