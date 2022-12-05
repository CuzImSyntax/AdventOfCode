from typing import List


def get_sums() -> List[int]:
    with open("input.txt", "r") as file:
        lines: List[str] = file.read().split("\n")

    sums: list = [0]
    index: int = 0
    for line in lines:
        if line == "":
            index += 1
            sums.append(0)
        else:
            sums[index] += int(line)

    return sums


def part_one() -> int:
    return max(get_sums())


def part_two() -> int:
    return sum(sorted(get_sums())[-3:])


if __name__ == "__main__":
    print(part_one())
    print(part_two())