num = int(input())
n1 = num-1
n2 = num+1
if(n1%6==0 or n2%6==0):
    print("Prime Number")
else:
    print("Not a prime number")