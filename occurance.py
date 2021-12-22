#5.	Please write a program which count and print the numbers of each character in a string input by console.
inputString = input("Enter a string: ").casefold()

tempStr = ''
for char in inputString:
    if char not in tempStr:
        print(char, ':',inputString.count(char))
        tempStr = tempStr+char

# output:
# Enter a string: sangeet
# s : 1
# a : 1
# n : 1
# g : 1
# e : 2
# t : 1      