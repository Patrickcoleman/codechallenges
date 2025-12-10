import math

input = open("advent2025/9/data.txt")

points = []

for line in input:
    raw_line = line.strip().split(",")
    points.append([int(point) for point in raw_line])

print(points)

best = 0

for i in range(len(points)):
    for j in range(i + 1, len(points), 1):
        size = abs(points[i][0] - points[j][0] + 1) * abs(points[i][1] - points[j][1] + 1)
        #print(f"Comparing point {i}: {points[i]} with point {j}: {points[j]}, area {size}")
        best = max(best, size)

print(best)