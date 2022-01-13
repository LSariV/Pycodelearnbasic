mylist = [2,1,3]

#using for loop

total = 1

for i in mylist:
    total = total *i
print("product of all elemnets using traversal is " , total)


# import numpy module to use numpy.prod

import math
list1 =[1, 2, 3]
list2 = [3, 2, 4]
 
# using numpy.prod() to get the multiplications
result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)