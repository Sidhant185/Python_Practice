# Q15: Simple calculator with four operations
# Performs addition, subtraction, multiplication, or division based on operator

# Input: Get operator from user (take first character)
operator = input("Enter Operator: ")[0]

# Input: Get first number
n1 = int(input("Enter a number: "))

# Input: Get second number
n2 = int(input("Enter a number: "))

# Check operator and perform corresponding operation
if(operator == '*'):
    # Multiplication
    print(n1*n2)
elif(operator == '/'):
    # Division
    print(n1/n2)
elif(operator == '+'):
    # Addition
    print(n1+n2)
elif(operator == '-'):
    # Subtraction
    print(n1-n2)
else:
    # Invalid operator
    print("Invalid")