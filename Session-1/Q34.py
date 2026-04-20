sum = 0
num = int(input())
for i in range(1,num+1):
    if(sum>=100):
        break
    else:
        sum = sum+i

print(sum)