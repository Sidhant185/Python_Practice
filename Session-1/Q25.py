# Q25: Find nth Fibonacci number
# Uses iterative approach to calculate Fibonacci sequence

# Input: Get position from user
num = int(input("Enter a number: "))

# Initialize first two Fibonacci numbers
n1 = 0
n2 = 1

# Loop num times to generate Fibonacci sequence
for i in range(num):
    # Calculate next Fibonacci number
    temp = n1+n2
    # Shift values for next iteration
    n1 = n2
    n2 = temp

# Output: Print nth Fibonacci number
print(n1)
