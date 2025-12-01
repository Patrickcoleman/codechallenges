input = open("1data.txt")

data = []

for line in input:
    line_str = str(line).strip()
    data.append(line_str)

pos = 50
zeros = 0

for instr in data:
    dir = instr[0]
    dist = int(instr[1:])
    dist = dist * -1 if dir == 'L' else dist

    dist_to_0_up = 100 - pos
    dist_to_0_down = -100 if pos == 0 else (0 - pos) 

    if dist >= dist_to_0_up:
        moves_after_0 = dist - dist_to_0_up
        zeros += 1 + (moves_after_0) // 100
    elif dist <= dist_to_0_down:
        moves_after_0 = dist - dist_to_0_down
        zeros += 1 + ((moves_after_0) * -1) // 100
        
    print(f"pos {pos}, dist {dist}, zeros {zeros}")

    pos = (pos + dist) % 100

print(zeros)


