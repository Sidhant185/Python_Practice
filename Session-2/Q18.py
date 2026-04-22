text = input()
vowels = "aeiouAEIOU"
v = 0
c = 0
for char in text:
    if char.isalpha():
        if char in vowels:
            v = v+1
        else:
            c = c+1

print(v)
print(c)