"""
WORKER'S PARTITION PROBLEM
Given N tasks, K workers and time taken for each task.
Find min time in which we can complete all the tasks
Rules:
1. A single worker can only do continuous set of tasks
2. All workers start their assigned tasks at same time
3. A task can only be assigned to one worker
"""
arr = [3, 5, 1, 7, 8, 2, 5, 3, 10, 1, 4, 7, 5, 4, 6]
n = len(arr)
k = 4
def check(A, N, K , T):
    count = 0
    total = 0
    for val in A:
        total += val
        if total > T:
            total = val
            count += 1
    if total != 0: count += 1
    if K >= count: return True
    return False

def min_time(A, N, K):
    low, high = max(A), sum(A)
    ans = 0
    while low <= high:
        mid = (low + high)//2
        if check(A, N, K, mid):
            ans = mid
            high = mid -1
        else: low = mid + 1
    return ans
print("min_time to complete all task: ", min_time(arr, n, k))