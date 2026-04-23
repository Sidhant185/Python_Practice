# Q10: Generate Pascal's Triangle
# Create triangle where each element is sum of two above

def generatePascal(numRows):
    """
    Generate Pascal's triangle with numRows rows
    Each element is sum of two elements above it
    Time Complexity: O(numRows^2)
    Space Complexity: O(numRows^2)
    """
    # Initialize empty triangle
    triangle = []
    
    # Build each row
    for i in range(numRows):
        # Initialize row with 1s
        # Each row has i+1 elements
        row = [1] * (i + 1)
        
        # Fill middle elements (not edges)
        for j in range(1, i):
            # Each middle element = sum of two above
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        # Add row to triangle
        triangle.append(row)
    
    return triangle