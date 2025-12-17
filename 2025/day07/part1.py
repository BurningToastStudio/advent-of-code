grid = []
next_grid_state = []
height = 0
width = 0


def setup_grid():
    global grid, height, width

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            row = list(line)
            grid.append(row)

    height = len(grid)
    width = len(grid[0])

    for i in range(width):
        if grid[0][i] == "S":
            grid[1][i] = "|"
            break

def splitter_below(x, y):
    if grid[y + 1][x] == "^":
        return True
    else:
        return False

total_splits = 0

def move_bar(x, y):
    global total_splits
    if splitter_below(x, y):
        try:

            next_grid_state[y + 1][x + 1] = "|"
            next_grid_state[y + 1][x - 1] = "|"
            total_splits += 1
        except IndexError:
            pass
    else:
        next_grid_state[y + 1][x] = "|"


setup_grid()

for y in range(height - 1):
    for x in range(width):
        next_grid_state = grid.copy()

        if grid[y][x] == "|":
            move_bar(x, y)
    grid[y] = next_grid_state[y].copy()

final_grid = "\n".join("".join(row) for row in grid)
print(final_grid)
print(total_splits)
