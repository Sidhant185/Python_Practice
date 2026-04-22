def swap(list, indx1, indx2):
    temp = list[indx1]
    list[indx1] = list[indx2]
    list[indx2] = temp

nums = list(map(int, input().split()))

i = 0
j = len(nums)-1
while(j>i):
    if(nums[i]==0):
        swap(nums, i, j)
        j  = j-1
    else:
        i = i+1

print(nums)