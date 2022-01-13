list1 = [10, 20, 4]

list2 = [20, 10, 20, 1, 100]

# Method1 sort the list as it will automatically 
# arrangesin ascending order and you can print first or last number

smallest =0
largest=0
 
list1.sort()
print("sortedlist is ", list1)
print("smallest element in the list is ", list1[1])
print("largest element in the list is ", list1[-1])

#using builtin methods 
#min() , max()

print("smallest using min ", min(list2))
print("largest using max ", max(list2))