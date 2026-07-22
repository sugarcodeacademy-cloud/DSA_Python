"""
Given N digits, Print all numbers that are formed using digist 1 and 2. Print numbers in increasing order
"""
N = 3
def printAll(arr, n, i):
    if i == n:
        print("".join(map(str,arr)))
        return

    arr[i] = 1
    printAll(arr, n, i+1)
    arr[i] = 2
    printAll(arr, n, i+1)

def solve(n):
    result = [0]*n
    printAll(result, n, 0)

print(solve(N))


print("************************End of 1st problem ****************************************")
"""
Given N digits, Print all numbers that are formed using digits first K digits starting from 1. Print numbers in increasing order
"""
N = 2
K = 5
def printAllK(arr, n, i, k):
    if i == n:
        print("".join(map(str,arr)))
        return

    for j in range(1, k+1):
        arr[i] = j
        printAllK(arr, n, i+1, k)

def solveK(n, k):
    result = [0]*n
    printAllK(result, n, 0, k)

print(solveK(N, 5))
