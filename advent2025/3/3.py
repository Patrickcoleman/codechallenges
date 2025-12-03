input = open("advent2025/3/3data.txt")

data = []

for line in input:
    line_str = str(line).strip()
    data.append(line_str)

bests = []

for bank in data:
    running = 0
    min_index = -1
    for x in range(12, 0, -1):
        highest = 0
        hightest_index = 0

        max_index = len(bank) - x
        for i in range(max_index, min_index,-1):
            if int(bank[i]) >= highest:
                hightest_index = i
                highest = int(bank[i])
        running = running * 10 + highest
        min_index = hightest_index

    bests.append(running)

print(bests)
print(sum(bests))


