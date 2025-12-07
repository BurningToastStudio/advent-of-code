fresh_start_range = []
fresh_end_range = []
available_ids = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    parse_fresh_ids = True

    for line in lines:
        line = line.strip()

        if line == "":
            parse_fresh_ids = False
            continue

        if parse_fresh_ids:
            start_range, end_range = line.split("-")
            fresh_start_range.append(int(start_range))
            fresh_end_range.append(int(end_range))
        else:
            available_ids.append(int(line))


fresh_available_ids = 0
for id in available_ids:
    id_fresh = False
    for i, value in enumerate(fresh_start_range):
        if fresh_start_range[i] <= id <= fresh_end_range[i]:
            id_fresh = True
            break
    if id_fresh:
        fresh_available_ids += 1

print(fresh_available_ids)



