# Q2: Nearby Duplicate
# Check if duplicate exists within distance k

def containsNearbyDuplicate(nums, k):
    """
    Find if array contains duplicate elements within distance k
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Dictionary to store last seen index of each number
    last_seen = {}
    
    # Iterate through array with indices
    for i, num in enumerate(nums):
        # Check if number was seen and is within distance k
        if num in last_seen and i - last_seen[num] <= k:
            return True
        
        # Update last seen index for this number
        last_seen[num] = i
    
    return False