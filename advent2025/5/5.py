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

print(range_data)

fresh_count = 0

for ingredient in ingredients:
    opens = 0
    for end in range_data:
        if ingredient == end[0]:
            fresh_count += 1
            break
        elif ingredient < end[0]:
            if opens:
                fresh_count += 1
            break
        else:
            if end[1] == 'O':
                opens += 1
            else:
                opens -= 1
print(fresh_count)
