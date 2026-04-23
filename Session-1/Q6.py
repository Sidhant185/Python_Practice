# Q6: Classify number as zero, positive, or negative
# Checks the sign of a number

# Input: Get number from user
n = int(input("Enter a number: "))

# Check if number equals zero
if(n == 0):
    print("Zero")
# Check if number is less than zero
elif(n<0):
    print("Negative")
# Number must be greater than zero
elif(n>0):
    print("Positive")