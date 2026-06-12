"""
AGGRESSIVE COWS PROBLEM
Given N cows and M stalls, all M stalls are placed on X-axis at different locations.
place all N cows such a way that minimum distance between any 2 cows is maximized
Rules:
1. In a stall only 1 cow should be present
2. All cows have to be placed
"""

#arr = [3, 8, 12, 18, 25, 30, 35, 41, 49]
arr =  [2, 6, 11, 14, 19, 25, 30, 39, 43]
m = 4

def check(A, M, K):
    count = 1
    last_cow = A[0]
    for i in range(1, len(A)):
        if A[i] - last_cow >= K:
            count += 1
            last_cow = A[i]
            if count == M: return True
    return False

def find_min_distance(A, M):
    A.sort()
    n = len(A)
    low , high = 0 , A[n-1] - A[0]
    ans = 0
    while low <= high:
        mid = (low + high)//2
        if check(A, M, mid):
            low = mid+1
            ans = mid
        else:
            high = mid - 1
    return ans
print("min distance between any 2 cows: ", find_min_distance(arr, m))