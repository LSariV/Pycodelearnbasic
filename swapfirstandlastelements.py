# how to swap first and last elements in ana array

# input: [4,6,2,8] output: [8,6,2,4]

# method 1 using temp variable
arr = [4,6,2,8]
temp = arr[0]
#print(first)  
leng = len(arr) # finding lenth of array to see how many elemnets are there
print(leng)

#last =arr[leng-1] # while retrieving numbers we should start with index 0 so lenth-1 will give last element
#print (last)
arr[0] = arr[leng-1]

arr[leng-1] = temp

print (arr)
 
 # second method 
 # we have shorcut in python...[0] is first position and [-1] is last element
arry=[7,5,4,2]
arry[0],arr[-1] = arry[-1], arry[0]
print (arry)
 
 #Approach 3 using touple..pending