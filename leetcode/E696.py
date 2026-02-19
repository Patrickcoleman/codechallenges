def countBinarySubstrings(s):
    count = 0

    for i in range(len(s)-1):
        j = i + 1
        while i > -1 and j < len(s) and s[i] == "0" and s[j] == "1":
            i -= 1
            j += 1
            count += 1
            
    for i in range(len(s)-1):
        j = i + 1
        while i > -1 and j < len(s) and s[i] == "1" and s[j] == "0":
            i -= 1
            j += 1
            count += 1

    return count

print(countBinarySubstrings("00110011"))