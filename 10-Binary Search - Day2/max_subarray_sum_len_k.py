#Given an array of +ve integers, find the maximum K such that,
#max of such subarray sum of len K <= B

arr = [3, 2, 5, 4, 6, 3, 7, 2]
b = 20


def max_subarray_sum_k(A, k):
    sub_sum = 0
    for j in range(k):
        sub_sum += A[j]
    max_sum = sub_sum
    for i in range(k, len(A)):
        sub_sum += A[i] - A[i-k]
        max_sum = max(sub_sum , max_sum)
    return max_sum

def find_k(A, B):
    low, high = 1, len(A)
    ans = 0
    while low <= high:
        k = (low + high)//2
        if max_subarray_sum_k(A ,k) <= B:
            ans = k
            low = k + 1
        else: high = k - 1
    return ans
print("find_k",find_k(arr, b))



