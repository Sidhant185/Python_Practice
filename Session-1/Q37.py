# Q37: Function to add two numbers
# Demonstrates function with return statement

# Input: Get first number
n1 = int(input())

# Input: Get second number
n2 = int(input())

# Define function to add two numbers
def add(n1, n2):
    # Calculate sum
    ans = n1+n2
    # Return the sum
    return ans

# Call function and print result
print(add(n1,n2))