# Q7: Rotate array by k positions
# Uses three reversals technique for efficient rotation

def swap(list, indx1, indx2):
    """
    Swap two elements at given indices
    """
    temp = list[indx1]
    list[indx1] = list[indx2]
    list[indx2] = temp

def rotate(list, indx1, indx2):
    """
    Reverse elements between two indices
    """
    while(indx2>indx1):
        swap(list, indx1, indx2)
        indx1 += 1
        indx2 -= 1

# Input: Get array from space-separated input
nums = list(map(int, input().split()))

# Input: Get rotation amount
k = int(input())

# Reverse entire array
rotate(nums,0,len(nums)-1)

# Reverse first k elements
rotate(nums,0,k-1)

# Reverse remaining elements
rotate(nums,k, len(nums)-1)

# Output: Print rotated array
print(nums)
