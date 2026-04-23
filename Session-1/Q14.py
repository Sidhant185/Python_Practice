# Q14: Check if number is divisible by 3
# Uses modulo operator to check divisibility

# Input: Get number from user
num = int(input("Enter a number "))

# Check if remainder when divided by 3 is zero
if(num%3==0):
    # Number is divisible by 3
    print("True")
else:
    # Number is not divisible by 3
    print("Not True")