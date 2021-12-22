# 10.Given numRows = 5,.

# Generate
# A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]

import math

def combination(n, r): 
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y):
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] 
    for count in range(rows): 
        row = [] 
        for element in range(count + 1): 
           
            row.append(combination(count, element))
        result.append(row)
      
    return result


for row in pascals_triangle(3):
    print(row)

# output:
# [1]
# [1, 1]
# [1, 2, 1]
