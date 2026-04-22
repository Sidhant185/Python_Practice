nums = []
size = int(input())
for k in range(size):
    nums.append(int(input()))

unique = []
for x in nums:
    if x not in unique:
        unique.append(x)

print(unique)