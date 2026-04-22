nums = []
size = int(input())
for i in range(size):
    nums.append(int(input()))

nums.sort()

print(nums[0])
print(nums[size-1])
