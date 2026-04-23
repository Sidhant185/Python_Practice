# Q23: Check if a number is palindrome
# Reverses number and compares with original

# Input: Get number from user
num = int(input("Enter a number: "))

# Initialize reverse to zero
rev = 0

# Save original number for comparison
temp = num

# Extract digits and build reverse number
while(temp>0):
    # Get last digit
    tem = temp%10
    # Add digit to reversed number
    rev = (rev*10)+tem
    # Remove last digit
    temp=temp//10

# Compare original with reverse
if(rev==num):
    # Numbers are same - palindrome
    print("True")
else:
    # Numbers are different - not palindrome
    print("False")