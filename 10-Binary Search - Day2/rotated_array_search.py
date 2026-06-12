#Given an array formed by rotating a distinct sorted by K times,
#search for a given element in a rotated array, if not found return -1

A=[11, 14, 19, 23, 27, -20, -14, -8, -4, 1, 2, 4, 7]
K= 5
B = 19

#Idea1:iterate over the array and find element B
def find_ele_rotated_sort_array_brute(arr, ele):
    for i,val in enumerate(arr):
        if val == ele:
            return i
    return -1
print("find_ele_rotated_sort_array_brute: ", find_ele_rotated_sort_array_brute(A, B))

#Idea2 : use binary search in first k elements and search in next k elements
def find_ele_rotated_sort_array_binary_search(arr, ele, k):
    def search_ele_binary_search(arr, ele, l, h):
        low = l
        high = h
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == ele:
                return mid
            elif arr[mid] > ele:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    first_arr = search_ele_binary_search(arr, ele, 0 , k-1)
    if first_arr == -1:
        second_arr = search_ele_binary_search(arr, ele, k , len(arr)-1)
    else : return first_arr
    return second_arr
print("find_ele_rotated_sort_array_binary_search: ", find_ele_rotated_sort_array_binary_search(A, B, K))

def find_ele_rotated_sort_array_binary_search_v2(arr, ele, k):
    def search_ele_binary_search(arr, ele, l, h):
        low = l
        high = h
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == ele:
                return mid
            elif arr[mid] > ele:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    if ele >= arr[0]:
        ans= search_ele_binary_search(arr, ele, 0 , k-1)
    else:
        ans = search_ele_binary_search(arr, ele, k , len(arr)-1)
    return ans
print("find_ele_rotated_sort_array_binary_search_v2: ", find_ele_rotated_sort_array_binary_search_v2(A, 2, K))
