def prefix_sum(nums, size):
    ans = []
    total = 0
    for i in range(size):
        total = total + nums[i]
        ans.append(total)
    return ans

nums = []
size = int(input())

for i in range(size):
    nums.append(int(input()))

sol = prefix_sum(nums, size)
print(sol)