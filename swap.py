# swapping two numbers

# num1 = 10
# num2 = 20


num1 = input("enter num1 value")
num2 = input("enter num2 value")

print("num1 value before swap", num1)
print("num2 value before swap", num2)

# Approach 1
# temp = num1
# num1 = num2
# num2 = temp

# print("values after swap", num1, num2, temp)


# swapping with out temp variable

# in python num1,num2=num2, num1 automaticalluy values are swapped

num1, num2 = num2, num1
print("values after swap", num1, num2)
