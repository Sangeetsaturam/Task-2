# 2.	Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

class String():
    def __init__(self):
        self.str = ""

    def get_String(self):
        self.str = input("Enter the name:")

    def print_String(self):
        print(self.str.upper())

str = String()
str.get_String()
str.print_String()

# output:
# sangeet
# SANGEET
