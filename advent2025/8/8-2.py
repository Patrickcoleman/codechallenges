import math

input = open("advent2025/8/data.txt")

points = []
connections = 1000

for line in input:
    raw_line = line.strip().split(",")
    points.append([int(point) for point in raw_line])

#print(points)

dists = []

for i in range(len(points)):
    for j in range(i + 1, len(points), 1):
        x_dist = points[j][0] - points[i][0]
        y_dist = points[j][1] - points[i][1]
        z_dist = points[j][2] - points[i][2]
        dist = math.sqrt(x_dist ** 2 + y_dist ** 2 + z_dist ** 2)
        dists.append([dist, i, j])

dists.sort()

circuits = [[i] for i in range(len(points))]

last_ids = []

while len(circuits) > 1:
    shortest = dists.pop(0)
    p1, p2 = shortest[1], shortest[2]
    last_ids = [p1, p2]
    p1_connection_index = None
    p2_connection_index = None
    for i in range(len(circuits)):
        if p1 in circuits[i]:
            p1_connection_index = i
        if p2 in circuits[i]:
            p2_connection_index = i
    
    if p1_connection_index != p2_connection_index:
        circuits[p1_connection_index] += circuits[p2_connection_index]
        circuits.pop(p2_connection_index)

print(last_ids)

