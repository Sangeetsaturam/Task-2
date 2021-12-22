
# 14. There are two arrays 
#        A = (1,2,3,4,5) the result should be 
#        B = (120,60,40,30,24)


def findProduct(A):
 
    # get length of the list
    n = len(A)
 
    # base case
    if n == 0:
        return
 
    # use two auxiliary lists
    left = [None] * n
    right = [None] * n
 
    # `left[i]` stores the product of all elements in sublist `A[0…i-1]`
    left[0] = 1
    for i in range(1, n):
        left[i] = A[i - 1] * left[i - 1]
 
    # `right[i]` stores the product of all elements in sublist `A[i+1…n-1]`
    right[n - 1] = 1
    for j in reversed(range(n - 1)):
        right[j] = A[j + 1] * right[j + 1]
 
    # replace each element with the product of its left and right sublist
    for i in range(n):
        A[i] = left[i] * right[i]
 
 
if __name__ == '__main__':
    A = []
    n = int(input("Enter the list size "))

    
    for i in range(0, n):
        print("Enter number at index", i, )
        item = int(input())
        A.append(item)
    print("User list is ", A)
 
    
    findProduct(A)
 
    # print the modified list
    print(A)


# Output:
# Enter the list size 5
# Enter number at index 0
# 2
# Enter number at index 1
# 3
# Enter number at index 2
# 4
# Enter number at index 3
# 5
# Enter number at index 4
# 6
# User list is  [2, 3, 4, 5, 6]
# [360, 240, 180, 144, 120]