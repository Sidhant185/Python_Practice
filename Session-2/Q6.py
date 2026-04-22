nums = list(map(int, input().split()))
size = len(nums)
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)
unique.sort()
print(unique[size-2])