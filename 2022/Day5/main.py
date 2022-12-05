from typing import Iterator
import re

def get_data() -> tuple[dict[int, list[str]], list[list[int]]]:
    with open("input.txt", "r") as file:
        lines: Iterator[str] = iter(file.read().split("\n"))

    stacks: dict[int, list[str]] = dict()
    for line in lines:
        if line == "":
            break
        for count, char in enumerate(line):
            if char.isalpha():
                count = int(count / 4) + 1
                if stacks.get(count):
                    stacks.get(count).append(char)
                else:
                    stacks[count] = [char]

    pattern: re.Pattern = re.compile(r'\d+')
    commands = []
    for line in lines:
        commands.append([int(number) for number in pattern.findall(line)])

    return dict(sorted(stacks.items())), commands

def move_crates(reversed_: bool = True) -> str:
    stacks: dict[int, list[str]]
    commands: list[list[int]]
    stacks, commands = get_data()

    for command in commands:
        crates = reversed(stacks.get(command[1])[:command[0]]) if reversed_ else stacks.get(command[1])[:command[0]]
        stacks.get(command[2])[:0] = crates
        stacks[command[1]] = stacks[command[1]][command[0]:]

    message: str = ""
    for stack in stacks.values():
        message += stack[0]
    return message

def part_one() -> str:
    return move_crates()

def part_two() -> str:
    return move_crates(False)

if __name__ == "__main__":
    print(part_one())
    print(part_two())