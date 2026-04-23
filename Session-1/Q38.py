# Q38: Function to check if number is even or odd
# Returns string description of number type

# Input: Get number from user
num = int(input())

# Define function to check if even or odd
def check(num):
    # Check remainder when divided by 2
    if(num%2==0):
        # Number is even
        return "Even"
    else:
        # Number is odd
        return "Odd"

# Call function and print result
print(check(num))