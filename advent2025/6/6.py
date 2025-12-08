input = open("advent2025/6/data.txt")

columns = []
operations = []

for line in input:
    line = line.strip()
    print(line)
    rawdata = line.split(' ')
    data = [num for num in rawdata if num != '']

    if '+' in line or '*' in line:
        operations = data
    else:
        if not columns:
            columns = [[] for _ in range(len(data))]
        for i in range(len(data)):
            columns[i].append(int(data[i]))

total = 0

for i in range(len(operations)):
    if operations[i] == '+':
        total += sum(columns[i])
    else:
        new = 1
        for num in columns[i]:
            new *= num
        total += new


print(columns)
print(operations)
print(total)

    
