# Take the list data from user and append it, ask for element to verify the precence

list = [2,4,'apple',4,5,'sonam']

print( " enter the lements in the list")
list.append(int(input()))
print(list)

print("which element you want to check in list")
ele = int(input())

counter =0

for i in list:
    if (i==ele):
        counter = counter +1
if (counter == 0):
    print("sorry element is not found")
else:
    print("elemenetr is present for this many times", counter)
    
    # simple method to iterate through the list values and check for element using 'in' or 'not in' operators
    
    if (ele in list):
        print ("found")
    else:
        print("sorry not found")