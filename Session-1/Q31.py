# Q31: Calculate GCD (Greatest Common Divisor)
# Uses Euclidean algorithm with modulo operation

# Input: Get first number
num1 = int(input())

# Input: Get second number
num2 = int(input())

# Euclidean algorithm: repeatedly apply modulo until num2 becomes 0
while(num2!=0):
    # Save current num2
    temp = num2
    # Replace num2 with remainder
    num2 = num1%num2
    # Replace num1 with previous num2
    num1 = temp

# Output: num1 now contains GCD
print(num1)