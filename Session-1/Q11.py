year = int(input("Enter a year: "))

if((year%4==0 and year%100) or (year%400) ):
    print("true")
else:
    print("false")