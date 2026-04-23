# Q12: Find intersection of two arrays
# Uses set operations to find common elements

# Input: Get first array from space-separated input
nums1 = list(map(int, input().split()))

# Input: Get second array from space-separated input
nums2 = list(map(int, input().split()))

# Find intersection using set operations
# Convert to sets and use & operator for intersection
inter = list(set(nums1)& set(nums2))

# Output: Print common elements
print(inter)