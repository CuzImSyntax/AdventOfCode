def get_data() -> str:
    with open("input.txt", "r") as file:
         line: str = file.readline()
    return line


def get_marker(range_: int) -> int:
    line: str = get_data()
    for i in range(0, len(line)):
        if len(set(line[i:i+range_])) == range_:
            return i+range_

def part_one() -> int:
    return get_marker(4)

def part_two() -> int:
    return get_marker(14)

if __name__ == "__main__":
    print(part_one())
    print(part_two())