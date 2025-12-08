input = open("advent2025/4/data.txt")

data = []
dirs = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [1, -1],
    [-1, 1],
    [1, 1],
    [-1, -1]
]

for line in input:
    line = str(line).strip()
    ind = []
    for char in line:


        
        ind.append(char)
    data.append(ind)

removed_total = 0

def remove_rolls(data):
    rolls_removed = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '@':
                continue    

            adj = 0

            for dir in dirs:
                newx, newy = i + dir[0], j + dir[1]
                if newx >= 0 and newx < len(data):
                    if newy >= 0 and newy < len(data[i]):
                        if data[newx][newy] == '@' or data[newx][newy] == 'x':
                            adj += 1
            
            if adj < 4:
                rolls_removed += 1
                data[i][j] = 'x'
    return rolls_removed

while True:
    new_removals = remove_rolls(data)
    removed_total += new_removals

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'x':
                data[i][j] = '.' 
    if new_removals == 0:
        break

print(removed_total)

