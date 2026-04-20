num = int(input("Enter a number: "))

n1 = 0
n2 = 1

for i in range(num):
    temp = n1+n2
    n1 = n2
    n2 = temp

print(n1)
