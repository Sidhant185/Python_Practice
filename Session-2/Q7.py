def swap(list, indx1, indx2):
    temp = list[indx1]
    list[indx1] = list[indx2]
    list[indx2] = temp

def rotate(list, indx1, indx2):
    while(indx2>indx1):
        swap(list, indx1, indx2)
        indx1 += 1
        indx2 -= 1


nums = list(map(int, input().split()))
k = int(input())

rotate(nums,0,len(nums)-1)
rotate(nums,0,k-1)
rotate(nums,k, len(nums)-1)

print(nums)
