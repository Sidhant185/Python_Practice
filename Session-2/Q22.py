text1 = input()
freq = {}
for char in text1:
    freq[char] = freq.get(char, 0)+1

for char in text1:
    if freq[char] == 1:
        print(char)
        break