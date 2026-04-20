num = int(input())

def count(num):
    sum = 0
    while(num>0):
        temp = num%10
        sum = sum+temp
        num = num//10

    return sum

print(count(num))
