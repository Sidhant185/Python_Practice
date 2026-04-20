num = int(input("Enter a number: "))
rev = 0
temp = num
while(temp>0):
    tem = temp%10
    rev = (rev*10)+tem
    temp=temp//10

if(rev==num):
    print("True")
else:
    print("False")