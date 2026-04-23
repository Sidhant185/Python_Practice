# Q32: Calculate LCM (Least Common Multiple)
# Uses formula: LCM = (a*b) / GCD(a,b)
# First calculates GCD using Euclidean algorithm

# Input: Get first number
num1 = int(input())

# Save original first number
temp1 = num1

# Input: Get second number
num2 = int(input())

# Save original second number
temp2 = num2

# Calculate GCD using Euclidean algorithm
while(num2!=0):
    temp = num2
    num2 = num1%num2
    num1 = temp

# num1 now contains GCD
gcd = num1

# Calculate LCM using formula
lcm = (temp1*temp2)//gcd

# Output: Print LCM
print(lcm)