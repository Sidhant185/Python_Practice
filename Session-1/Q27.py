# Q27: Print inverted triangle pattern with asterisks
# First row has num asterisks, decreases each row

# Input: Get number of rows from user
num = int(input("Enter a number: "))

# Outer loop from num down to 1
for i in range(num,0,-1):
    # Inner loop to print asterisks for current row
    for j in range(i):
        # Print asterisk without newline
        print("*", end="")
    # Move to next line
    print()
    