num1 = int(input())
temp1 = num1
num2 = int(input())
temp2 = num2

while(num2!=0):
    temp = num2
    num2 = num1%num2
    num1 = temp

gcd = num1
lcm = (temp1*temp2)//gcd
print(lcm)