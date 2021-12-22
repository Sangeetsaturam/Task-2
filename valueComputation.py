#3.	Write a program that computes the value of a+aa+aaa with a given digit as the value of a.

digit=int(input("Enter digit:"))
num=input("enter a number:")
 
result=0
for i in range(1,digit+1):
  result= result + int(str(num*i))
 
print(result)

# output:
# Enter digit:3
# enter a number:3
# 369