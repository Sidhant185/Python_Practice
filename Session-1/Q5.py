# Q5: Check if a number is even or odd
# Uses modulo operator to determine divisibility by 2

# Input: Get number from user
n = int(input("Enter a number: "))

# Check remainder when divided by 2
if(n%2==0):
    # If remainder is 0, number is even
    print("Even")
else:
    # If remainder is 1, number is odd
    print("Odd")