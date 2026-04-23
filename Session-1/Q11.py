# Q11: Check if a year is leap year
# Leap year: divisible by 4 AND (not divisible by 100 OR divisible by 400)

# Input: Get year from user
year = int(input("Enter a year: "))

# Check leap year conditions:
# A year is leap if: (divisible by 4 and NOT 100) OR (divisible by 400)
if((year%4==0 and year%100) or (year%400) ):
    print("true")
else:
    print("false")