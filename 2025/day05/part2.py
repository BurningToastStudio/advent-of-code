ranges = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            break
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

ranges.sort(key=lambda x: x[0])

merged = []

for start, end in ranges:
    if not merged:
        merged.append([start, end])
        continue

    last_start, last_end = merged[-1]

    if end < last_start:
        merged.append([start, end])

    elif start > last_end:
        merged.append([start, end])

    elif start <= last_end:
        merged[-1][1] = max(last_end, end)

total_diff = 0
for start, end in merged:
    total_diff += end - start + 1

print(total_diff)
