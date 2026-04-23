# Q33: Print numbers from 1 to 50 excluding multiples of 3
# Uses continue statement to skip specific iterations

# Loop from 1 to 50 (inclusive)
for i in range(1, 51):
    # Check if number is divisible by 3
    if(i%3==0):
        # Skip this number and go to next iteration
        continue
    else:
        # Print numbers not divisible by 3
        print(i)