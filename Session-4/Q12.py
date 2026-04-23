# Q12: Hourglass Sum
# Find maximum sum of hourglass pattern in matrix

def hourglassSum(matrix):
    """
    Find maximum sum of hourglass pattern (3x3 shape)
    Hourglass: top row + middle + bottom row
    Time Complexity: O(m*n)
    Space Complexity: O(1)
    """
    # Initialize max sum to negative infinity
    max_sum = float('-inf')
    
    # Iterate through all possible hourglass positions
    # Can't start in last 2 rows or columns
    for r in range(len(matrix) - 2):
        for c in range(len(matrix[0]) - 2):
            # Top row of hourglass (3 elements)
            top = sum(matrix[r][c:c+3])
            
            # Middle element
            mid = matrix[r+1][c+1]
            
            # Bottom row of hourglass (3 elements)
            bot = sum(matrix[r+2][c:c+3])
            
            # Total hourglass sum
            hourglass_sum = top + mid + bot
            
            # Update maximum
            max_sum = max(max_sum, hourglass_sum)
    
    return max_sum