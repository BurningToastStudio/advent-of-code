total = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()

        best = 0

        for i in range(len(line)):
            digit_1 = int(line[i])
            for j in range(i + 1, len(line)):
                digit_2 = int(line[j])
                val = digit_1 * 10 + digit_2
                if val > best:
                    best = val
        total += best

print(total)
