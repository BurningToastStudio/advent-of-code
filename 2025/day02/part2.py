import textwrap
invalid_ids_sum = 0

with open("input.txt", "r") as file:
    text = file.readline()
    id_pairs = text.split(",")
    for id_pair in id_pairs:
        id_start, id_end = id_pair.split("-")

        for i in range(int(id_start), int(id_end) + 1):
            id = str(i)

            max_pattern = len(id) // 2
            pattern_width = 1

            while pattern_width <= max_pattern:
                if len(id) % pattern_width != 0:
                    pattern_width += 1
                    continue

                split_id = textwrap.wrap(id, pattern_width)
                if len(set(split_id)) == 1:
                    invalid_ids_sum += i
                    break
                pattern_width += 1

print(invalid_ids_sum)