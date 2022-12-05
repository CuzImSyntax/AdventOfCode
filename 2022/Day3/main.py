from typing import List, Set

PRIO: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_data() -> List[str]:
    with open("input.txt", "r") as file:
        lines: List[str] = file.read().split("\n")
    return lines

def part_one() -> int:
    sum_: int = 0
    for line in get_data():
        chars: Set[str] = set(line[:len(line)//2]) & set(line[len(line)//2:])
        for char in chars:
            sum_ += PRIO.find(char) + 1

    return sum_

def part_two() -> int:
    sum_: int = 0
    data: List[str] = get_data()
    for i in range(0, len(data), 3):
        char = set(data[i]) & set(data[i+1]) & set(data[i+2])
        sum_ += PRIO.find(char.pop()) + 1

    return sum_

if __name__ == "__main__":
    print(part_one())
    print(part_two())