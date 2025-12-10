input = open("advent2025/9/data.txt")

points = []

for line in input:
    raw_line = line.strip().split(",")
    points.append([int(point) for point in raw_line])

# #print(points)

oppsites = {
    'U' : 'D',
    'L' : 'R',
    'R' : 'L',
    'D' : 'U'
}

oob_points = []

prev_dir = 'L'
last_corner = None

for i in range(len(points) - 1):
    j = i + 1
    x1, x2 = points[i][0], points[j][0]
    y1, y2 = points[i][1], points[j][1]
    if x2 > x1:
        next_dir = 'R'
    elif x1 > x2:
        next_dir = 'L'
    elif y2 > y1:
        next_dir = 'D'
    else:
        next_dir = 'U'

    current_corner = None
    
    if prev_dir == 'L':
        if next_dir == 'U':
            current_corner = [x1 - 1, y1 - 1]
        elif next_dir == 'D':
            current_corner = [x1 + 1, y1 - 1]
    elif prev_dir == 'U':
        if next_dir == 'R':
            current_corner = [x1 + 1, y1 - 1]
        elif next_dir == 'L':
            current_corner = [x1 + 1, y1 + 1]
    elif prev_dir == 'R':
        if next_dir == 'D':
            current_corner = [x1 + 1, y1 + 1]
        elif next_dir == 'U':
            current_corner = [x1 - 1, y1 + 1]
    elif prev_dir == 'D':
        if next_dir == 'L':
            current_corner = [x1 - 1, y1 + 1]
        elif next_dir == 'R':
            current_corner = [x1 - 1, y1 - 1]
    
    if last_corner and current_corner:
        xs = [last_corner[0], current_corner[0]]
        xs.sort()
        ys = [last_corner[1], current_corner[1]]
        ys.sort()
        x1, x2 = xs[0], xs[1]
        y1, y2 = ys[0], ys[1]

        if x2 > x1:
            for x in range(x1, x2 + 1):
                oob_points.append([x, y1])
        else:
            for y in range(y1, y2 + 1):
                oob_points.append([x1, y])
    
    if not current_corner:
        print("WTF")
    
    last_corner = current_corner

    prev_dir = oppsites[next_dir]


best = 0

for i in range(len(points) - 1):
    print(f"Up to starting point {i}/{len(points)}")
    for j in range(i + 1, len(points) - 1, 1):
        xs = [points[i][0], points[j][0]]
        xs.sort()
        ys = [points[i][1], points[j][1]]
        ys.sort()
        x1, x2 = xs[0], xs[1]
        y1, y2 = ys[0], ys[1]

        size = (x2 - x1 + 1) * (y2 - y1 + 1)

        if size > best:
            forbidden = False
            for barrier in oob_points:
                if barrier[0] >= x1 and barrier[0] <= x2 and barrier[1] >= y1 and barrier[1] <= y2:
                    #print(f"Big square size {size} from {points[i][0]}, {points[i][1]} to {points[j][0]}, {points[j][1]} broken by barrier {barrier}")
                    forbidden = True
                    break
            if not forbidden:
                #print(f"new biggest square from {points[i][0]}, {points[i][1]} to {points[j][0]}, {points[j][1]}, area: {size}")
                best = size

matrix = [['.' for i in range(20)] for j in range(20)]

for x in range(20):
    for y in range(20):
        if [x, y] in points:
            matrix[y][x] = '#'
        elif [x, y] in oob_points:
            matrix[y][x] = 'X'

for i in range(20):
    line_string = f"{matrix[i]} \n"
    print(matrix[i])

print(best)