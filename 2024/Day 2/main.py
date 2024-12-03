import os

def is_safe(report: list[int]) -> bool:

    is_descending: bool = False

    for i in range(len(report) - 1):
        current: int = report[i]
        next_val: int = report[i + 1]

        if i == 0:
            if next_val > current:
                is_descending = False
            else:
                is_descending = True
        else:
            if is_descending and next_val > current:
                return False
            elif not is_descending and next_val < current:
                return False

        if 1 <= abs(next_val - current) <= 3:
            continue
        return False

    return True

current_dir = os.path.dirname(__file__)

filename = "input.txt"
file_path = os.path.join(current_dir, filename)

with open(file_path, "r") as f:
    lines = [line.strip() for line in f.readlines()]

data = [
    line.split(" ")
    for line in lines
]
data = [
    [int(x) for x in line]
    for line in data
]

counter: int = 0 

for row in data:
    if is_safe(row):
        counter += 1


print(f"Safe Rows: {counter}")


## Part Two

def is_safe_with_removal(report: list[int]):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

counter: int = 0

for row in data:
    if is_safe(row):
        counter += 1
    else:
        if is_safe_with_removal(row):
            counter += 1

print(f"Safe Rows: {counter}")