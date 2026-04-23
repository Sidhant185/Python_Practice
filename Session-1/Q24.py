# Q24: Print multiplication table of a number
# Uses for loop to print products from 1 to 10 times

# Input: Get number from user
num = int(input("Enter a number: "))

# Loop from 1 to 10 (inclusive)
for i in range(1, 11):
    # Print number multiplied by loop counter
    print(num*i)