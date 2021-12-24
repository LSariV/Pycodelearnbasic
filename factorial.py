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
    
    
    # factorial of a number using resurcive approach
    
    # n! = n* (n-1)* (n-2)* ....1
    # 4! = 4* (4-1)* (4-2)*(4-3)
    
    num2 = int(input("enter num2 "))
    
    def factorial(num2):
        if (num2==0 or num2==1):
            return 1
        else:
            return num2 * factorial(num2-1)
        
print("factorial of your number using recurrive method " , factorial(num2))
        