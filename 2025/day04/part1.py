array = []
allowed_rolls = 0

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

for i in range(rows):
    for j in range(cols):

        if array[i][j] == ".":
            continue

        rolls = 0

        for delta_row, delta_col in neighbours:
            new_row = i + delta_row
            new_col = j + delta_col
            if new_row < 0 or new_col < 0:
                continue
            try:
                if array[new_row][new_col] == "@":
                    rolls += 1
            except IndexError:
                pass # yes this is terrible, yes it works, no I will not apologise

        if rolls < 4:
            allowed_rolls += 1

print(allowed_rolls)
