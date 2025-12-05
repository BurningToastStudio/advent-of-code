invalid_ids_sum = 0

with open("input.txt", "r") as file:
    text = file.readline()
    id_pairs = text.split(",")
    for id_pair in id_pairs:
        id_start, id_end = id_pair.split("-")

        for i in range(int(id_start), int(id_end) + 1):
            id = str(i)
            mid = len(id) // 2
            if id[:mid] == id[mid:]:
                invalid_ids_sum += i

print(invalid_ids_sum)