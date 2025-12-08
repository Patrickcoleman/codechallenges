input = open("advent2025/6/data.txt")

data = []

for line in input:
    characters = line.strip('\n')
    sep_chars = []
    for char in characters:
        sep_chars.append(char)
    data.append(sep_chars)

print(data)
total = 0
column_numbers = []

for i in range(len(data[0]) - 1, -1, -1):
    current_number = 0
    for j in range(len(data)):
        char = data[j][i]
        print(print(f"Char is {char}"))
        if char == ' ':
            if current_number:
                print(f"Adding {current_number} to column numbers")
                column_numbers.append(current_number)
                current_number = 0
        elif char in ['*', '+']:
            if current_number:
                column_numbers.append(current_number)
            current_number = 0
            print(f"Summing column, numbers {column_numbers}")
            new = 0
            if char == '+':
                new = sum(column_numbers)
            else:
                addition = 1
                for num in column_numbers:
                    addition = addition * num
                new = addition
            print(f"Adding {new} to total {total}")
            total += new
            column_numbers = []
        else:
            current_number = current_number * 10 + int(char)

print(total)


