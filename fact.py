# 5! = 5*4*3*2*1
#n! = n* (n-1)*(n-2)* (n-3)*...1


num = 5
def fact(num):
 for i in range(1,num+1):
      return num*fact(num-i)
      