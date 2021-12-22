#15.convert a decimal number to binary using recursion.
def decToBin(x):
    str=''
    if x > 1:
        decToBin(x//2)
    print (x%2, end='')

num=int(input("Enter a number:"))
decToBin(num)

#Output:
# Enter a number:3
# 11