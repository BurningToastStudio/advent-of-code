import re

with open("input.txt", "r") as file:
    text = file.read()

mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
matches = re.findall(mul_pattern, text)

total = 0
for x, y in matches:
    total += int(x) * int(y)

print(total)
