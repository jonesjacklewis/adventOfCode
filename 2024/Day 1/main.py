import os

from dataclasses import dataclass

@dataclass
class datapoint:
    point_1: list[int]
    point_2: list[int]

def load_data() -> list[str]:
    with open(input_filepath, "r") as file:
        return file.read().splitlines()

def convert_data_to_data_point(data: list[str]) -> datapoint:

    point_1: list[int] = []
    point_2: list[int] = []

    for point in data:
        points = point.split("   ")

        if len(points) != 2:
            raise ValueError("Invalid data")
        
        point_1_str: str = points[0]
        point_2_str: str = points[1]

        point_1_str = point_1_str.replace("(", "").replace(")", "").strip()
        point_2_str = point_2_str.replace("(", "").replace(")", "").strip()

        if not point_1_str.isdigit() or not point_2_str.isdigit():
            raise ValueError("Invalid data")
        
        point_1.append(int(point_1_str))
        point_2.append(int(point_2_str))

    return datapoint(point_1 = point_1, point_2 = point_2)

current_dir: str = os.path.dirname(__file__)

input_filename: str = "input.txt"
input_filepath: str = os.path.join(current_dir, input_filename)

data: list[str] = load_data()
formatted_data: datapoint = convert_data_to_data_point(data)

point_1: list[int] = formatted_data.point_1
point_2: list[int] = formatted_data.point_2

if len(point_1) != len(point_2):
    raise ValueError("Invalid data")

point_1.sort()
point_2.sort()

differeneces: list[int] = []

for i in range(len(point_1)):
    differeneces.append(abs(point_1[i] - point_2[i]))

total_difference: int = sum(differeneces)

print(f"Total difference: {total_difference}")


# Part 2

similarity_score: int = 0
score_lookup: dict[int, int] = {}

for num in point_1:
    if num in score_lookup:
        similarity_score += score_lookup[num]
    else:
        increase_by = num * point_2.count(num)
        similarity_score += increase_by
        score_lookup[num] = increase_by

print(f"Similarity score: {similarity_score}")