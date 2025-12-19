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

num_connections = 1000

for idx in range(num_connections):
    i, j, distance = connection_data[idx]
    union(i, j)

circuits = {}
for box in range(num_boxes):
    root = find(box)
    if root not in circuits:
        circuits[root] = []
    circuits[root].append(box)

circuit_sizes = []
for circuit in circuits.values():
    size = len(circuit)
    circuit_sizes.append(size)

circuit_sizes.sort(reverse=True)

result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
print(result)
