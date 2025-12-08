input = open("advent2025/7/data.txt")

data = []

for line in input:
    line = line.strip()
    data_line = [char for char in line]
    data.append(data_line)

splits = 0
beams = []

for line in data:
    print(f"New line, beams at {beams}, splits {splits}")
    new_beams = {}
    if "S" in line:
        new_beams[line.index("S")] = True
    else:
        for beam in beams:
            if line[beam] == "^":
                if beam < (len(line) - 1):
                    new_beams[beam + 1] = True
                    splits += 1
                if beam > (1):
                    new_beams[beam - 1] = True
            else:
                new_beams[beam] = True
    
    beams = []
    for key in new_beams.keys():
        beams.append(key)
    
print(splits)
            
                

