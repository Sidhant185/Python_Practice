# Q5: Minimize Height Difference II
# Minimize height difference with constraint on negative numbers

def getmin(arr, k):
    """
    Minimize height difference, skip if next element < 0
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    # Sort array
    arr.sort()
    n = len(arr)
    
    # Initialize with original difference
    ans = arr[-1] - arr[0]
    
    # Try each partition point
    for i in range(n-1):
        # Skip if next element is negative
        if arr[i+1] < 0: 
            continue
        
        # Calculate min and max with modifications
        mini = min(arr[0]+k, arr[i+1]-k)
        maxi = max(arr[-1]-k, arr[i]+k)
        
        # Update answer
        ans = min(ans, maxi-mini)
    
    return ans

# Input and output
nums = list(map(int, input()))
target = int(input())
print(getmin(nums, target))