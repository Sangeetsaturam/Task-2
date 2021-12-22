 #11. Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d    = target? Find all unique quadruplets in the array which gives the sum of target.
def quadTuple(A, target):
    A.sort()

    for i in range(len(A) - 3):
        for j in range(i + 1, len(A) - 2):
            k = target - (A[i] + A[j])
            low = j + 1
            high = len(A) - 1
 
            while low < high:
                if A[low] + A[high] < k:
                    low = low + 1
                elif A[low] + A[high] > k:
                    high = high - 1
                # quadruplet with a given sum found
                else:
                    print((A[i], A[j], A[low], A[high]))
                    (low, high) = (low + 1, high - 1)

A = [-2, 0, 1, 2, -1, 0]
target = 0
quadTuple(A, target)