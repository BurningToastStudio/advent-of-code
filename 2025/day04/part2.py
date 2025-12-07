import copy

array = []

with open("input.txt", "r") as file:
    for line in file:
        array.append(list(line.strip()))

rows = len(array)
cols = len(array[0])

neighbours = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

total_removed = 0

while True:
    removed_this_round = []

    for i in range(rows):
        for j in range(cols):

            if array[i][j] == ".":
                continue

            neighbor_count = 0
            for delta_row, delta_col in neighbours:
                new_row = i + delta_row
                new_col = j + delta_col

                if 0 <= new_row < rows and 0 <= new_col < cols: # :)
                    if array[new_row][new_col] == "@":
                        neighbor_count += 1

            if neighbor_count < 4:
                removed_this_round.append((i, j))

    if not removed_this_round:
        break

    for i, j in removed_this_round:
        array[i][j] = "."

    total_removed += len(removed_this_round)

print(total_removed)
