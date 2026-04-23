# Q10: Grade assignment based on marks
# Assigns letter grades based on score ranges

# Input: Get marks from user
marks = int(input("Enter your Marks: "))

# Determine grade using if-elif conditions
if(marks>=90):
    # Grade A for marks >= 90
    print("A")
elif(marks<90 and marks>=75):
    # Grade B for marks between 75 and 89
    print("B")
elif(marks<75):
    # Grade C for marks below 75
    print("c")