n1 = int(input())
n2 = int(input())
n3 = int(input())

nums = []
nums.append(n1)
nums.append(n2)
nums.append(n3)
print(nums)

largest = n1
for i in range(3):
    if(nums[i]>largest):
        largest = nums[i]

print(largest)