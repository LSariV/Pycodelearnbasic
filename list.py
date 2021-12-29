#https://websitesetup.org/wp-content/uploads/2021/04/Python-cheat-sheet-April-2021.pdf
fruits = ['apple', 'orange']
print (fruits)
fruits.append('grapes')
print(fruits)

fruits.insert(1,'berry')
print (fruits)

fruits.remove('apple')
print (fruits)
fruits.pop()
print(fruits)

#combine two lists

tropical = ['mango','guava']

allfruits = fruits +tropical
print(allfruits)

#sorting

numlist = [6,17,4,0,2,1]
numlist.sort()
print(numlist)

#slice [startingindex : up to what index+1]

numlist[0:2]
print(numlist[0:2])

# List slicing 

list1 = ['s', 'i', 'r', 'i','d','e','e','p']
listreverse = list1[::-1]
print(listreverse)

print (10*(5+6))