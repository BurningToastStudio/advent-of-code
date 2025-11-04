chars_array = []

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
        case "upright":
            return row - 1, col + 1
        case "downleft":
            return row + 1, col - 1
        case "downright":
            return row + 1, col + 1

def is_valid_index(row, col):
    if 0 <= row < len(chars_array) and 0 <= col < len(chars_array[0]):
        return True
    return False

def check_around_char(row, col, target_char, specific_direction):
    new_r, new_c = move_index(row, col, specific_direction)
    if is_valid_index(new_r, new_c):
        if chars_array[new_r][new_c] == target_char:
            return True
        return False
    return False

def check_char(row, col, target_char):
    if is_valid_index(row, col):
        if chars_array[row][col] == target_char:
            return True
    return False


xmas_count = 0
for row_idx in range(len(chars_array)):
    for col_idx in range(len(chars_array[row_idx])):
        if check_char(row_idx, col_idx, "A"):

            found_1 = check_around_char(row_idx, col_idx, "M", "upleft")
            found_2 = check_around_char(row_idx, col_idx, "S", "downright")

            found_3 = check_around_char(row_idx, col_idx, "S", "upleft")
            found_4 = check_around_char(row_idx, col_idx, "M", "downright")

            found_5 = check_around_char(row_idx, col_idx, "M", "upright")
            found_6 = check_around_char(row_idx, col_idx, "S", "downleft")

            found_7 = check_around_char(row_idx, col_idx, "S", "upright")
            found_8 = check_around_char(row_idx, col_idx, "M", "downleft")

            if (found_1 and found_2) or (found_3 and found_4):
                if (found_5 and found_6) or (found_7 and found_8):
                    xmas_count += 1

print(xmas_count)
