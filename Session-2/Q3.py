nums = []
size = int(input())
for i in range(size):
    nums.append(int(input()))
even = 0
odd = 0
for j in range(size):
    if(nums[j]%2==0):
        even = even+1
    else:
        odd = odd+1

print(even)
print(odd)