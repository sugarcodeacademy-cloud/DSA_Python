#Given an array formed by rotating a distinct sorted by K times,
#Find K

A=[9, 11, 14, 19, 23, 27, -20, -14, -8, -4, 1, 2, 4, 7]

def find_rotations(arr):
    low , high = 0 , len(arr) -1
    k = 0
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < arr[0]:
            k = mid
            high = mid -1
        else:
            low = mid + 1
    return k
print("find_rotations :", find_rotations(A))