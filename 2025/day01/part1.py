numbers = []
directions = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        directions.append(line[0])
        numbers.append(line[1:])
def move_dial(dir, amount):
    global current_num
    amount = int(amount)

    for i in range(amount):
        if dir == "L":
            current_num -= 1
        else:
            current_num += 1

        if current_num == 100:
             current_num = 0
        elif current_num == -1:
            current_num = 99

    return current_num

current_num = 50
zero_count = 0

for i in range(len(directions)):
    if move_dial(directions[i], numbers[i]) == 0:
        zero_count += 1

print(zero_count)