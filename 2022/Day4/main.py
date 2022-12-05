from typing import List, Tuple
import re

def get_data() -> List[str]:
    with open("input.txt", "r") as file:
        lines: List[str] = file.read().split("\n")
    return lines

def get_ranges() -> List[Tuple[range]]:
    pattern: re.Pattern = re.compile(r'\d+')
    result : List[Tuple[range]] = []
    for line in get_data():
        (a, b, c, d) = (int(number) for number in pattern.findall(line))
        result.append((range(a, b+1), range(c, d+1)))
    return result

def part_one() -> int:
    sum_: int = 0
    for line in get_ranges():
        intersection = len(set(line[0]) & set(line[1]))
        if intersection == len(line[0]) or intersection == len(line[1]):
            sum_ += 1

    return sum_

def part_two() -> int:
    sum_: int = 0
    for line in get_ranges():
        if set(line[0]) & set(line[1]):
            sum_ += 1

    return sum_

if __name__ == "__main__":
    print(part_one())
    print(part_two())