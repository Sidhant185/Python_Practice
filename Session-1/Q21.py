# Q21: Count number of digits in a number
# Uses division by 10 in a loop to extract digits

# Input: Get number from user
num = int(input("Enter number: "))

# Initialize digit counter
count = 0

# Process number digit by digit
while(num>0):
    # Remove last digit by integer division
    num = num//10
    # Increment count for each digit
    count = count+1

# Output: Print digit count
print(count)