# Q15: Flatten 2D matrix into 1D array
# Converts nested list structure to single list

# Initialize empty matrix
matrix = []

# Input: Get number of rows
m = int(input())

# Input: Read each row of matrix
for i in range(m):
    matrix.append(list(map(int, input().split())))

# Flatten matrix using list comprehension
# Iterates through rows, then items in each row
flat = [item for row in matrix for item in row]

# Output: Print flattened array
print(flat)