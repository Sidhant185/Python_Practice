num = int(input())

def check(num):
    if(num<3):
        return "prime"
    if(num%6==1 or num%6==5):
        return "prime"
    else:
        return "Not Prime"

print(check(num))