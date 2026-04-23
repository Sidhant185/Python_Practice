# Q39: Function to find maximum of two numbers
# Compares two numbers and returns larger one

# Input: Get first number
n1 = int(input())

# Input: Get second number
n2 = int(input())

# Define function to find maximum
def max(n1,n2):
    # Check which number is larger
    if(n1>n2):
        # Return first number
        return n1
    else:
        # Return second number
        return n2

# Call function and print result
print(max(n1,n2))