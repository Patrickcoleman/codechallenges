input = open("advent2025/2/2data.txt")

text_raw = input.read()
text = text_raw.strip()
pairs_raw = text.split(",")

pairs = []
for pair in pairs_raw:
    string_pair = pair.split("-")
    pairs.append([string_pair[0], string_pair[1]])

palindromes = []

for pair in pairs:
    for i in range(int(pair[0]), int(pair[1]) + 1):
        digits = len(str(i))
        first = i // (10 ** (digits // 2))
        second = i % (10 ** (digits // 2))
        if first == second:
            palindromes.append(i)

print(palindromes)
print(sum(palindromes))


# def count_palindomes_between_nums(num1, num2):
#     len_str = len(num1)
#     palindromes = 0

#     if len(num1) != len(num2):
#         print("Unaccounted for case")
#     else:
#         if len(num1) % 2 == 0:
#             half = len_str//2
#             str1_half1 = num1[0:half]
#             str2_half1 = num2[0:half]
#             str1_half2 = num1[half:]
#             str2_half2 = num2[half:]

#             str1_half_int = int(str1_half1)
#             str2_half_int = int(str2_half1)
#             str1_half2_int = int(str1_half2)
#             str2_half2_int = int(str2_half2)

#             palindromes = str2_half_int - str1_half_int - 1
#             palindromes += 1 if (str1_half2 <= str1_half1) else 0
#             palindromes += 1 if (str2_half2 >= str2_half1) else 0

#     return palindromes

# total_palindromes = 0

# for pair in pairs:
#     while(len(pair[1]) > len(pair[0])):
#         floor = 10 ** (len(pair[1]) - 1)
#         total_palindromes += count_palindomes_between_nums(str(floor), pair[1])
#         pair[1] = str(floor - 1)
#     total_palindromes += count_palindomes_between_nums(pair[0], pair[1])

# print(total_palindromes)