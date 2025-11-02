left = []
right = []
similaritys = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    lines_amount = len(lines)
    for line in lines:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

for i in range(len(left)):
    count = 0
    left_num = left[i]
    for j in range(len(left)):
        right_num = right[j]
        if right_num == left_num:
            count += 1
    similaritys.append(left_num * count)

score = sum(similaritys)
print(score)
