# you should remove the nth occurance word from the given list 

list = ['grapes', 'mangoes','berrys', 'fruits','mangoes','raspberry']
#list.remove('mangoes')
#list.pop(3)
#del list[0]
print(list)

word = 'mangoes'
n=2

count =0

for i in range(0 , len(list)-1):
    if (list[i] == word):
        count = count + 1
        if (count == n):
          del list[i]
    count = count + 1
print(list)