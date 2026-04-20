num1 = int(input())
num2 = int(input())

while(num2!=0):
    temp = num2
    num2 = num1%num2
    num1 = temp

print(num1)