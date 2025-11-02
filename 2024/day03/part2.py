import re

with open("input.txt", "r") as file:
    text = file.read()

total = 0
enabled = True

for match in re.finditer(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)|do\(\)|don't\(\)", text):
    instruction = match.group(0)

    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled:
            x, y = match.groups()
            total += int(x) * int(y)

print(total)
