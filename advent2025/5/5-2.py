input = open("advent2025/5/data.txt")

ranges = []
ingredients = []

for line in input:
    line = str(line).strip()
    if "-" in line:
        data = line.split("-")
        start, stop = int(data[0]), int(data[1])
        ranges.append([start, stop])
    else:
        if len(line) < 1:
            continue
        data = int(line)
        ingredients.append(data)

print(ranges)
print(ingredients)

range_data = []

for range in ranges:
    range_data.append([range[0], 'O'])
    range_data.append([range[1], 'C'])

range_data.sort()
range_data_sorted = sorted(range_data, key=lambda x: (x[0], -ord(x[1])))

print(range_data)
print(range_data_sorted)

fresh_range = 0
opens = 0
open_begin = None

for end in range_data_sorted:
    if end[1] == 'O':
        if open_begin != None:
            open_begin = min(open_begin, end[0])
        else:
            open_begin = end[0]

        opens += 1
    else:
        opens -= 1
        if opens == 0:
            fresh_range += end[0] - open_begin + 1
            print(f"Closing final open at pos {end[0]}, added {end[0] - open_begin + 1} potential freshes")
            open_begin = None

print(fresh_range)


