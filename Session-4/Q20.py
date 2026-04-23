# Q20: Buddy Strings
# Check if strings can be made equal by swapping at most two characters

def buddyStrings(s, goal):
    """
    Check if s can be converted to goal by swapping at most two characters
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Strings must have same length
    if len(s) != len(goal): 
        return False
    
    # If strings are equal, need at least one duplicate for swapping
    if s == goal:
        # If has duplicate character, we can swap them
        return len(set(s)) < len(s)
    
    # Find positions where characters differ
    diffs = [i for i in range(len(s)) if s[i] != goal[i]]
    
    # Must have exactly 2 differences for single swap
    if len(diffs) != 2: 
        return False
    
    # Check if swapping these two positions makes strings equal
    i, j = diffs
    return s[i] == goal[j] and s[j] == goal[i]