"""
Given N tasks to complete
1. Deadline assigned for each task should be completed on or before the deadline
2. Payment for each task is assigned
3.On any give day, you can perform only one task

Find the MAX PAYMENT you can get
"""

A=[(2,200),(1,250),(1,200),(1,350),(4,300),(5,100),(4,250),(5,600), (5,400),(2,150)]

import heapq
def max_payment(tasks):
    min_heap = []
    heapq.heapify(min_heap)
    n = len(tasks)
    tasks.sort(key = lambda x:x[0])
    for task in tasks:
        deadline, payment = task
        if deadline > len(min_heap):
            heapq.heappush(min_heap, payment)
        elif payment > min_heap[0]:
            heapq.heapreplace(min_heap,payment)
    return sum(min_heap)

print(f'max payment = {max_payment(A)}')
