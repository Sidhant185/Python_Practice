text = input()
freq = {}
for char in text:
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1


for ch,num in freq.items():
    print(ch,num)