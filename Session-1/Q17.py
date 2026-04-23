# Q17: Print all even numbers from 1 to 100
# Uses loop with modulo operator for filtering

# Loop from 1 to 100
for i in range(1,101):
    # Check if number is even (divisible by 2)
    if(i%2==0):
        # Print even numbers
        print(i)