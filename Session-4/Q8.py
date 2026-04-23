# Q8: Check Toeplitz Matrix
# Matrix where each diagonal has same value

def isToeplitzMatrix(matrix):
    """
    Check if matrix is Toeplitz (all diagonals have same element)
    Time Complexity: O(m*n)
    Space Complexity: O(1)
    """
    # Check all diagonals by comparing with top-left neighbor
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            # Each element must equal its diagonal neighbor
            if matrix[r][c] != matrix[r-1][c-1]:
                return False
    
    return True