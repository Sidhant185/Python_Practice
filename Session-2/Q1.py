# Q1: Calculate prefix sum array
# Prefix sum: each element is sum of all elements up to that position

def prefix_sum(nums, size):
    """
    Calculate prefix sum of array
    Args:
        nums: input array
        size: size of array
    Returns:
        Array where each element is cumulative sum up to that index
    """
    ans = []
    total = 0
    # Iterate through each element
    for i in range(size):
        # Add current element to total
        total = total + nums[i]
        # Append cumulative sum to result
        ans.append(total)
    return ans

# Input: Get size of array
nums = []
size = int(input())

# Input: Get array elements
for i in range(size):
    nums.append(int(input()))

# Call function and print result
sol = prefix_sum(nums, size)
print(sol)