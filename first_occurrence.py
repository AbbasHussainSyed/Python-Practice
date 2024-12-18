#  modified binary search algorithm to find the first index in the array
def first_occurrence(arr, val, low, high):
    #  base case
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == val:
        if mid == 0 or arr[mid - 1] < val:
            return mid
        else:
            return first_occurrence(arr, val, low, mid - 1)
    elif arr[mid] > val:
        return first_occurrence(arr, val, low, mid - 1)
    else:
        return first_occurrence(arr, val, mid + 1, high)


arr = [1, 2, 3, 3, 4, 5, 6, 6]
result = first_occurrence(arr, 3, 0, len(arr) - 1)
print(result)

#  time complexity of O(logn)
