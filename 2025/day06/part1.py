import math
array = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        array.append(line.split())

calculations = []

for i in range(len(array[0])):
    new_row = []
    for j in range(len(array)):
        num = array[j][i]
        new_row.append(num)
    calculations.append(new_row)

total = 0
for row in calculations:
    if row[-1] == "+":
        del row[-1]
        nums = list(map(int, row))
        total += sum(nums)
    else:
        del row[-1]
        nums = list(map(int, row))
        total += math.prod(nums)

print(total)

