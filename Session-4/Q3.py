# Q3: Garden Plot Allocation
# Check if k new plants can be placed without adjacent plants

def canPlaceFlowers(flowerbed, k):
    """
    Determine if k flowers can be planted without adjacency
    0 = empty, 1 = occupied
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Counter for flowers planted
    count = 0
    
    # Add padding of zeros at both ends for boundary handling
    # This simplifies logic as we don't need special cases for edges
    f = [0] + flowerbed + [0]
    
    # Check each position from index 1 to n-1 (ignoring padding)
    for i in range(1, len(f) - 1):
        # Can plant if current and neighbors are empty
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            # Plant flower
            f[i] = 1
            count += 1
    
    # Check if we can plant at least k flowers
    return count >= k