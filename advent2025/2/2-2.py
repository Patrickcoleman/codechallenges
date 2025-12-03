input = open("advent2025/2/2data.txt")

text_raw = input.read()
text = text_raw.strip()
pairs_raw = text.split(",")

pairs = []
for pair in pairs_raw:
    string_pair = pair.split("-")
    pairs.append([string_pair[0], string_pair[1]])

palindromes = {}

for pair in pairs:
    for i in range(int(pair[0]), int(pair[1]) + 1):
        istr = str(i)
        digits = len(istr)
        for j in range(1, digits):
            if digits % j == 0:
                base = istr[:j]
                allwork = True
                for x in range(0, digits//j):
                    if istr[j * x: j * x + j] != base:
                        allwork = False
                        break
                if allwork:
                    palindromes[i] = 1

print(palindromes)
print(sum(palindromes))

