left = []
right = []
number_diffs = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

left.sort()
right.sort()

for i in range(len(left)):
    number_diffs.append(abs(left[i] - right[i]))

total = sum(number_diffs)
print(total)
