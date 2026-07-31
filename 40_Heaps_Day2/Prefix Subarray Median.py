"""
Given an array of size N, find the median for all prefix subarray (subarray starting with 0)
"""
from heapq import heappush, heapreplace, heappop

A=[3, 4, 16, 12, 10, 14, 8, 9, 2, 1]
B = [4, 9, 6, 2, 1, 10, 9, 7, 3, 5]

def median(arr):
    left =[]
    right = []
    median = []


    for num in arr:
        # Insert into appropriate heap
        if left and num <= -left[0]:
            heappush(left, -num) #maxHeap so we are mutliplying by -1
        else:
            heappush(right, num)

        # Balancing heaps
        if len(left) - len(right) == -1:
            heappush(left, -heappop(right))
        elif len(left) - len(right) > 1:
            heappush(right, -heappop(left))

        #Find median
        if len(left) == len(right):
            median.append((-left[0] + right[0])/2)
        else:
            median.append(-left[0])

    return median

print(median(B))