# Q13: Find all pairs that sum to target
# Uses set for O(n) lookup of complements

def findp(arr, target):
    """
    Find all unique pairs that sum to target
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Set to track seen numbers
    seen = set()
    # Set to store unique pairs (avoid duplicates)
    pair = set()

    # Iterate through array
    for num in arr:
        # Calculate what we need to reach target
        complement = target- num
        
        # If complement was seen, we found a pair
        if complement in seen:
            # Store pair with smaller first (to maintain uniqueness)
            pair.add((min(num, complement), max(num, complement)))
        
        # Add current number to seen set
        seen.add(num)
    
    return list(pair)

# Input: Get array from space-separated input
nums = list(map(int, input().split()))

# Input: Get target sum
target = int(input())

# Call function and print result
print(findp(nums, target))