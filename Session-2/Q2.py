# Q2: Find minimum and maximum elements in array
# Sorts array and accesses first and last elements

# Initialize empty list
nums = []

# Input: Get size of array
size = int(input())

# Input: Read all array elements
for i in range(size):
    nums.append(int(input()))

# Sort array in ascending order
nums.sort()

# Output: Print minimum (first element after sort)
print(nums[0])

# Output: Print maximum (last element after sort)
print(nums[size-1])
