# Find factorial of a given number
factorial =1
num = int(input("enter the number to find factorial"))

if num < 0:
    print("sorry we cannot find factorial for  -ve number")
elif num == 0:
    print("factorial of zero is always 1")
else:
    for i in range (1,num+1):
        factorial = factorial * i
    print("factorial of the given number ", num, "is", factorial )
    