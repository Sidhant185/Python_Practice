operator = input("Enter Operator: ")[0]
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

if(operator == '*'):
    print(n1*n2)
elif(operator == '/'):
    print(n1/n2)
elif(operator == '+'):
    print(n1+n2)
elif(operator == '-'):
    print(n1-n2)
else:
    print("Invalid")