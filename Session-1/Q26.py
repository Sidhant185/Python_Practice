# Q26: Print right triangle pattern with asterisks
# Each row i contains i asterisks

# Input: Get number of rows from user
num = int(input("Enter a number: "))

# Outer loop for each row
for i in range(1,num+1):
    # Inner loop to print asterisks in current row
    for j in range(i):
        # Print asterisk without newline
        print("*", end="")
    # Move to next line after each row
    print()
    