# 1) Using sum() Method
#Sum(iterable, start)
#more details in onenote

mylist = [3,1,4,6]

sumList = sum(mylist)
print(sumList)

#with start, here start is not index, instead start is the number to which the list sum is added,default value is zero

sumlist1 = sum(mylist,2)
print(sumlist1)

# using for loop

numSum =0 
for i in mylist:
    numSum+= i;
print("sum of the number in the list using for loop ", numSum)

#using While Loop

def listsum(mylist):
    i=0
    totalsum=0
    while i <len(mylist):
        totalsum+= mylist[i]
        i+=1
    return totalsum

totalsumoflist = listsum(mylist)
print("while loop ", totalsumoflist)

#Sum of List Containing String Value
 
#Using for loop
# Declare list of numbers as string
numlist3 = ['2','4','2','5','7','9','23','4','pap']
# Calculate sum of list

numsum1=0
for i in numlist3:
    numsum1 = numsum1+ int(i)
print('sum of list of strings', numsum1)
