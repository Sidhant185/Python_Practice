# Q19: Calculate factorial of a number
# Uses for loop with multiplication accumulator

# Input: Get number from user
num = int(input())

# Initialize factorial to 1
fact = 1

# Loop from 1 to num (inclusive)
for i in range(1,num+1):
    # Multiply current number with factorial
    fact = fact*i

# Output: Print factorial
print(fact)