def swap(list, indx1, indx2):
    temp = list[indx1]
    list[indx1] = list[indx2]
    list[indx2] = temp

nums = []
size = int(input())
for k in range(size):
    nums.append(int(input()))

i = 0
j = size-1
while(j>i):
    swap(nums, i, j)
    i += 1
    j -= 1

print(nums)
