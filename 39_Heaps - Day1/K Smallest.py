"""
Given an array of size N, with N distinct elements, find the smallest K elements in the array, where K<N
"""
import heapq

A = [8, 3, 10, 4, 11, 2, 7, 6, 5, 1]
K = 4

def k_smallest(arr, k):
    if k<=0: return []

    max_heap = []

    for i in range(0,k):
        heapq.heappush(max_heap, -arr[i])

    for i in range(k, len(arr)):
        if arr[i] < -max_heap[0]:
            heapq.heapreplace(max_heap, -arr[i])

    return sorted(-x for x in max_heap)

print("first k smallest elements in array are: ", k_smallest(A, K))

