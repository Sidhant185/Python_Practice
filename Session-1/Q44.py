num = int(input())
def prime(num):
    ans = []
    for i in range(1, num+1):
        if(i<3):
            ans.append(i)
        elif(i%6==1 or i%6==5):
            ans.append(i)
    
    return ans

print(prime(num))