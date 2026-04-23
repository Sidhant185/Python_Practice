# Q18: Count Binary Substrings
# Count substrings with equal 0s and 1s (e.g., "0011", "01")

def countBinarySubstrings(s):
    """
    Count contiguous substrings with equal 0s and 1s
    Each valid substring has pattern: 0s followed by 1s (or vice versa)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Group consecutive same characters
    groups = []
    count = 1
    
    # Build groups of consecutive characters
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            # Same character, increment count
            count += 1
        else:
            # Different character, save group and reset
            groups.append(count)
            count = 1
    
    # Don't forget last group
    groups.append(count)
    
    # Count valid substrings
    # Each valid substring is min of adjacent groups
    res = 0
    for i in range(1, len(groups)):
        res += min(groups[i], groups[i-1])
    
    return res