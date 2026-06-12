"""
Every element occur twice except for 1, find unique elements
Note: Duplicates are adjacent to each other
"""

A = [3,3,1,1,8,8,10,10,19,6,6,2,2,4,4]

#idea 1: iterate over the array and use xor
def find_unique_brute(arr):
    unique = 0
    for val in arr:
        unique ^= val
    return unique
print("find_unique_brute: ", find_unique_brute(A))

#idea 2: Use binary search, first occurrence on left of unique number are at even index and on right are at odd index
def find_unique_binary_search(arr):
    n = len(arr)
    if n==1: return arr[0]
    if arr[0] != arr[1]: return arr[0]
    if arr[n-1] != arr[n-2]: return arr[n-1]
    low, high = 1, n-2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] != arr[mid -1] and arr[mid] != arr[mid+1]: return arr[mid]
        if arr[mid] == arr[mid -1] : mid -= 1
        if mid % 2 == 0:
            low = mid + 2
        else:
            high = mid -1
print("find_unique_binary_search: ", find_unique_binary_search(A))
