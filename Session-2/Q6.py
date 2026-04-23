# Q6: Find second largest unique element in array
# Gets unique elements, sorts, and returns second-to-last

# Input: Get array from space-separated input
nums = list(map(int, input().split()))

# Get size of array
size = len(nums)

# Initialize unique list
unique = []

# Iterate through numbers to find unique elements
for x in nums:
    # Add if not already in unique list
    if x not in unique:
        unique.append(x)

# Sort unique elements in ascending order
unique.sort()

# Output: Print second largest (size-2 index after sorting)
print(unique[size-2])