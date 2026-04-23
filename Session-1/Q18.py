# Q18: Calculate sum of numbers from 1 to n
# Uses for loop with accumulator pattern

# Input: Get number from user
num = int(input())

# Initialize sum to zero
sum = 0

# Loop from 1 to num (inclusive)
for i in range(1,num+1):
    # Add current number to sum
    sum = sum+i

# Output: Print total sum
print(sum)