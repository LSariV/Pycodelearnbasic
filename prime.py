# check number is prime or not
# Prime number rules:

# Number >1 and number only has 2 factors 1 and itself

# num =12
num = int(input(" enter num "))
count = 0

print("num you entered ", num)
if num > 1:

    # for i in range(1,num+1):
    #    if(num%i) == 0:
    #        count = count +1

    #  if count ==2:
    #      print("your number is prime number")

    #  else:
    #      print("sorry your number is not prime")

    # other method

    for i in range(2, num):
        #print("value of i is " , i)
        if (num % i) == 0:
            print("is not prime")
            break

    else:
        print("num is prime number")
