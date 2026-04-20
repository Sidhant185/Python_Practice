age = int(input("Enter your age: "))
if(age<0):
    print("invalid age")
elif(age<13):
    print("Child")
elif(age>=13 and age<=19):
    print("Teen")
else:
    print("Adult")