# Q4: Reverse array by swapping elements from both ends
# Uses two-pointer approach to swap pairs

def swap(list, indx1, indx2):
    """
    Swap two elements in list by their indices
    Args:
        list: the list to swap in
        indx1: first index
        indx2: second index
    """
    temp = list[indx1]
    list[indx1] = list[indx2]
    list[indx2] = temp

# Initialize empty list
nums = []

# Input: Get size of array
size = int(input())

# Input: Read all array elements
for k in range(size):
    nums.append(int(input()))

# Initialize pointers from both ends
i = 0
j = size-1

# Swap elements moving towards center
while(j>i):
    # Swap current pair
    swap(nums, i, j)
    # Move pointers towards center
    i += 1
    j -= 1

# Output: Print reversed array
print(nums)
