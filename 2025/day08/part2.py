import math

box_positions = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for vec in lines:
        vec = vec.strip().split(",")
        new_vec = []
        for pos in vec:
            new_pos = int(pos)
            new_vec.append(new_pos)
        box_positions.append(new_vec)

def find_distance(vec1, vec2):
    point1 = (vec1[0], vec1[1], vec1[2])
    point2 = (vec2[0], vec2[1], vec2[2])
    return math.dist(point1, point2)

connection_data = []
for i in range(len(box_positions)):
    for j in range(i + 1, len(box_positions)):
        vec1 = box_positions[i]
        vec2 = box_positions[j]
        distance = find_distance(vec1, vec2)
        connection_data.append((i, j, distance))

connection_data.sort(key=lambda x: x[2])

num_boxes = len(box_positions)
parent = list(range(num_boxes))

def find(box):
    if parent[box] != box:
        parent[box] = find(parent[box])
    return parent[box]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False

def total_circuits():
    roots = set()
    for box in range(num_boxes):
        roots.add(find(box))
    return len(roots)

last_connection = ()
for i, j, distance in connection_data:
    if union(i, j):
        last_connection = (box_positions[i], box_positions[j])
        if total_circuits() == 1:
            break

result = last_connection[0][0] * last_connection[1][0]
print(result)
