# Q10: Move all zeros to end while maintaining order
# Swaps zeros with non-zero elements from right

def swap(list, indx1, indx2):
    """
    Swap two elements at given indices
    """
    temp = list[indx1]
    list[indx1] = list[indx2]
    list[indx2] = temp

# Input: Get array from space-separated input
nums = list(map(int, input().split()))

# Initialize pointers from both ends
i = 0
j = len(nums)-1

# Use two-pointer approach to move zeros
while(j>i):
    # Check if current element is zero
    if(nums[i]==0):
        # Swap zero with element from right
        swap(nums, i, j)
        # Move right pointer towards left
        j  = j-1
    else:
        # Move left pointer towards right
        i = i+1

# Output: Print array with zeros at end
print(nums)