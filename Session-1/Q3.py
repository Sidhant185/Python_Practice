# Q3: Check if person is adult or minor
# Determines age category based on age threshold of 18

# Input: Get age from user
age = int(input("Enter your age: "))

# Check if age is 18 or above
if (age>=18):
    # Person is adult
    print("Adult")
else:
    # Person is minor
    print("Minor")
