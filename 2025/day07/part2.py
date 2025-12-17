grid = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        grid.append(list(line))


height = len(grid)
width = len(grid[0])

start_row = 0
start_col = None

for col in range(width):
    if grid[0][col] == "S":
        start_col = col
        break

grid_memory = {}

def count_timelines(row, col):
    if row + 1 >= height:
        return 1

    if (row, col) in grid_memory:
        return grid_memory[(row, col)]

    below_cell = grid[row + 1][col]

    if below_cell != "^":
        result = count_timelines(row + 1, col)

    else:
        left_count = count_timelines(row + 1, col - 1)
        right_count = count_timelines(row + 1, col + 1)

        result = left_count + right_count

    grid_memory[(row, col)] = result

    return result

answer = count_timelines(start_row, start_col)

print(answer)
