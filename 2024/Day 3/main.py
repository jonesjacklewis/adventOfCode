import re

def extract_mul_from_line(line: str) -> list[str]:
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

    results = pattern.findall(line)

    return results

def solve_mul(mul: str) -> int:
    pattern = re.compile(r"\d{1,3}")

    multipliers = pattern.findall(mul)

    result: int = 1

    for num in multipliers:
        result *= int(num)

    return result

with open("input.txt", "r") as f:
    inp = f.read()

results = extract_mul_from_line(inp)

total: int = 0

for result in results:
    total += solve_mul(result)

print(total)

## Part Two


def extract_muls_part_two(line: str) -> list[str]:

    mul_enabled = True

    pattern = re.compile(r"(don't\(\)|do\(\))")

    arr = pattern.split(line)

    muls: list[str] = []

    for value in arr:
        if value == "don't()":
            mul_enabled = False
        elif value == "do()":
            mul_enabled = True
        else:
            if mul_enabled:
                matched_muls = extract_mul_from_line(value)
                muls.extend(matched_muls)

    return muls


results = extract_muls_part_two(inp)

total = 0

total: int = 0

for result in results:
    total += solve_mul(result)

print(f"Total {total}")