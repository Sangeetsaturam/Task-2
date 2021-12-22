def longestCommonPrefix(a):
    size = len(a)
    if (size == 0):
        return "Null"
 
    if (size == 1):
        return a[0]

    print(a)
     
    # find the minimum length from
    # first and last string
    end = min(len(a[0]), len(a[size - 1]))
 
    # find the common prefix between
    # the first and last string
    i = 0
    while (i < end and a[0][i] == a[size - 1][i]):
        i += 1
 
    pre = a[0][0: i]
    return pre
 
# Driver Code
if __name__ == "__main__":
    array = []
    while True:
        a = input()
        if not a:
            break
        array.append(a);
    print("The longest Common Prefix is :" ,longestCommonPrefix(array))

# output:
# abcs
# abc
# ab
# abcdef

# ['ab', 'abc', 'abcdef', 'abcs']
# The longest Common Prefix is : ab