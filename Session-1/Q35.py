# Q35: Simple number guessing game
# User keeps guessing until correct number is found

# Input: Get target number from system
num = int(input())

# Initialize play flag
play = True

# Continue looping while play is True
while(play):
    # Input: Get user's guess
    num1 = int(input())
    
    # Check if guess matches target
    if (num1==num):
        # Correct guess
        print("Correct Guess")
        # Set flag to False to exit loop
        play = False
        break