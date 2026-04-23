# Q9: Check if number is divisible by both 3 and 5
# Uses compound condition with logical AND

# Input: Get number from user
num = int(input("Enter a number: "))

# Check if number is divisible by both 3 AND 5
if(num%3==0 and num%5==0):
    # Both conditions are true
    print("True")
else:
    # At least one condition is false
    print("False")
    