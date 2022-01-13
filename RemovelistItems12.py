# clear fuctions for list elements 

mylist = [ 4, 6, 'poor', 9, 'good']


# remove() to memove specified item

mylist.remove('poor')
print(mylist)

#pop() deletes the specified index, if no index is specified deletes last one
mylist.pop(1)
print(mylist)

mylist.pop() #removes last one as no index is specified
print(mylist)

#clear() to clear the values from list
mylist.clear()
print(mylist)


#del keyword (not fn)