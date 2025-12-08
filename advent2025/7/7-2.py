input = open("advent2025/7/data.txt")

data = []

for line in input:
    line = line.strip()
    data_line = [char for char in line]
    data.append(data_line)

beams = {}

for line in data:
    print(f"New line, beams at {beams}")
    new_beams = {}
    if "S" in line:
        new_beams[line.index("S")] = 1
    else:
        for beam in beams.keys():
            if line[beam] == "^":
                if beam < (len(line) - 1):
                    new_beams.setdefault(beam + 1, 0)
                    new_beams[beam + 1] += beams[beam]
                if beam > 0:
                    new_beams.setdefault(beam - 1, 0)
                    new_beams[beam - 1] += beams[beam]
            else:
                new_beams.setdefault(beam, 0)
                new_beams[beam] += beams[beam]
    
    beams = new_beams.copy()
    
print(beams)
print(sum(beams.values()))










### Yeah, too slow vvvv

# data = []

# for line in input:
#     line = line.strip()
#     data_line = [char for char in line]
#     data.append(data_line)
# beams = []

# for i in range(len(data)):
#     print(f"Calcing line {i}")
#     line = data[i]
#     new_beams = []
#     if "S" in line:
#         new_beams.append(line.index("S"))
#     else:
#         for beam in beams:
#             if line[beam] == "^":
#                 if beam < (len(line) - 1):
#                     new_beams.append(beam+1)
#                 if beam > 0:
#                     new_beams.append(beam-1)
#             else:
#                 new_beams.append(beam)
    
#     beams = new_beams.copy()

# beams.sort()
# print(beams)
# print(len(beams))
            
                

