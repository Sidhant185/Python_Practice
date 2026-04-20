num = int(input())

def reverse(num):
    temp = num 
    rev = 0
    while(temp>0):
        tem = temp%10
        rev = (rev*10)+tem
        temp = temp//10
    return rev

print(reverse(num))