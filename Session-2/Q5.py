# Q5: Find all unique elements in array
# Maintains list and checks for duplicates

# Initialize empty list
nums = []

# Input: Get size of array
size = int(input())

# Input: Read all array elements
for k in range(size):
    nums.append(int(input()))

# Initialize unique list
unique = []

# Iterate through each element
for x in nums:
    # Check if element is not already in unique list
    if x not in unique:
        # Add new unique element
        unique.append(x)

# Output: Print list of unique elements
print(unique)