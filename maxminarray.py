# find max and min element in an array
# input : arr[1,9,6,8]
#output max: 9
#output min:1

arr = [ 1, 9, 6,5,8]

max = arr[0]
length = len(arr)

for i in range(1,length):
    
    if arr[i] > max:
        max = arr[i]
print(max)

# minimum number
min = arr[0]

for i in range(1, length):
    if arr[i] < min:
        min = arr[i]
        
print(min)

