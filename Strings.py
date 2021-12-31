str = "{1}  {0}  {2}" .format('geeks', 'oh' ,'shape')
print(str)

str2 = " hello this is me"
str2 = "{3} {1} {2} {0} ".format('hello','this','is','me')
print(str2)
str2 = "{m} {i} {t} {h} ".format(h='hello',t='this',i='is',m='me')
print(str2)

print (str2.upper())
print (str2.lower())
print(str2.replace('e','y'))
print(str2.find("i"))
print(str2.split())
print(str2.title())
print(str2.strip())