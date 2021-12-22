#13. Write a function that takes a list L and returns a sublist of size N of that list. Assume that the index is in a decreasing order.you cannot go frontwards


import random

def randomList(L,N):
    list = random.sample(L, N)
    list = sorted(list)
    return  list


if __name__ == '__main__':
    L=input("Enter the list:")
    N=int(input("Enter the number:"))
    sublist=randomList(L,N)
    print("Sub List={0}".format(sublist))

# output:
# Enter the list:1234
# Enter the number:3
# Sub List=['1', '2', '4']