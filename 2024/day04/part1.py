chars_array = []

"""
This may be painful to look at
if you are reading this, i am sorry
"""

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        row_chars = []
        for char in line:
            row_chars.append(char)
        chars_array.append(row_chars)

def move_index(row, col, dir):
    match dir:
        case "upleft":
            return row - 1, col - 1
        case "up":
            return row - 1, col
        case "upright":
            return row - 1, col + 1
        case "left":
            return row, col - 1
        case "right":
            return row, col + 1
        case "downleft":
            return row + 1, col - 1
        case "down":
            return row + 1, col
        case "downright":
            return row + 1, col + 1

def is_valid_index(row, col):
    if 0 <= row < len(chars_array) and 0 <= col < len(chars_array[0]):
        return True
    return False

def check_around_char(row, col, target_char, specific_direction):
    if specific_direction is not None:
        new_r, new_c = move_index(row, col, specific_direction)
        if is_valid_index(new_r, new_c):
            if chars_array[new_r][new_c] == target_char:
                return True, new_r, new_c, specific_direction
        return False, None, None, None

    directions = ["upleft", "up", "upright", "left", "right", "downleft", "down", "downright"]
    for dir_name in directions:
        new_r, new_c = move_index(row, col, dir_name)
        if is_valid_index(new_r, new_c):
            if chars_array[new_r][new_c] == target_char:
                return True, new_r, new_c, dir_name

    return False, None, None, None

def check_char(row, col, target_char):
    if is_valid_index(row, col):
        if chars_array[row][col] == target_char:
            return True
    return False


xmas_count = 0
for row_idx in range(len(chars_array)):
    for col_idx in range(len(chars_array[row_idx])):
        if check_char(row_idx, col_idx, "X"):

            directions = ["upleft", "up", "upright", "left", "right", "downleft", "down", "downright"]
            for dir_name in directions:
                found, r, c, d = check_around_char(row_idx, col_idx, "M", dir_name)
                if found:
                    found, r, c, d = check_around_char(r, c, "A", dir_name)
                    if found:
                        found, r, c, d = check_around_char(r, c, "S", dir_name)
                        if found:
                            xmas_count += 1

print(xmas_count)
