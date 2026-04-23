# Q28: Print number pattern triangle
# Each row i contains numbers from 1 to i-1

# Input: Get number of rows from user
num = int(input("Enter a number: "))

# Outer loop for rows (from 2 to num+1)
for i in range(2,num+2):
    # Inner loop to print numbers 1 to i-1
    for j in range(1,i):
        # Print number without newline
        print(j, end="")
    # Move to next line
    print()
    