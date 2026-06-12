#Given N, find the nearest floor of the square root of N
def square_root(N):
    low , high = 0 , N
    ans = 0
    while low <= high:
        mid = (low + high)//2
        square = mid*mid
        if square == N: return mid
        elif square > N: high = mid -1
        else:
            ans = mid
            low = mid + 1
    return ans
print("square_root :", square_root(37))